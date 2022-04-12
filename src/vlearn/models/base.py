"""Model base object class.

Support for automatic detection of CRUD operations.
Foreign key should be supplied manually.
"""
from PyQt5 import QtSql


class Model:
    """Base class for every model.
    """
    TABLE = ''
    CREATE_QUERY = ''
    PRIMARY_KEY = []
    ATTRIBUTES = []
    IGNORE_KEY = ('self', '__class__', '_Model__query_setval', '_Model__query_condpk')

    def __init__(self):
        """Generate new instance of model.
        """
        self.__query_setval = ', '.join([
            '`{}` = ?'.format(x)
            for x in self.__dict__
            if x not in self.PRIMARY_KEY
            and x not in self.IGNORE_KEY
        ])
        self.__query_condpk = ' AND '.join([
            '`{}` = ?'.format(x)
            for x in self.PRIMARY_KEY
        ])

    def save(self) -> bool:
        """Save the model to database.

        Returns:
            bool: True if the model is successfully saved.
        """
        query = QtSql.QSqlQuery()
        query.setForwardOnly(True)
        query.prepare("""
            UPDATE {}
            SET {}
            WHERE {}
        """.format(
            self.TABLE,
            self.__query_setval,
            self.__query_condpk
        ))
        for k, v in self.__dict__.items():
            if k not in self.IGNORE_KEY and k not in self.PRIMARY_KEY:
                query.addBindValue(v)
        for k in self.PRIMARY_KEY:
            query.addBindValue(self.__dict__[k])
        query.exec()
        return query.numRowsAffected() > 0

    def delete(self) -> bool:
        """Delete the model from database.

        Returns:
            bool: True if the model is successfully deleted.
        """
        query = QtSql.QSqlQuery()
        query.prepare("""
            DELETE FROM {} WHERE {}
        """.format(
            self.TABLE,
            self.__query_condpk
        ))
        for k in self.PRIMARY_KEY:
            query.addBindValue(self.__dict__[k])
        query.exec()
        return query.numRowsAffected() > 0

    @classmethod
    def __create_from_value(cls, value):
        """Create new instance of model from value iterator.

        Args:
            value (function): Positional getter valuefunction.

        Returns:
            Model: New instance of model.
        """
        return cls(**dict(zip(cls.ATTRIBUTES, [
            value(x) for x in range(len(cls.ATTRIBUTES))
        ])))

    @classmethod
    def get(cls, **kwargs):
        """Get model from database.

        Args:
            **kwargs: Lookup criteria for the model.

        Returns:
            Model: Model object if any.
        """
        res = None
        query = QtSql.QSqlQuery()
        query.setForwardOnly(True)
        where_stmt = ' AND '.join([
            '`{}` = ?'.format(k)
            for k, _ in kwargs.items()
        ])
        where_stmt = 'WHERE ' + where_stmt if where_stmt else ''
        query.prepare("""
            SELECT {} FROM {} {} LIMIT 1
        """.format(
            ', '.join([
                '`{}`'.format(x)
                for x in cls.ATTRIBUTES
            ]),
            cls.TABLE,
            where_stmt
        ))
        for _, v in kwargs.items():
            query.addBindValue(v)
        query.exec()
        if query.next():
            res = cls.__create_from_value(query.value)
        return res

    @classmethod
    def all(cls, **kwargs):
        """Get all models from database.

        Args:
            **kwargs: Lookup criteria for the model.

        Returns:
            list: List of models. Empty list if no model found.
        """
        res = []
        query = QtSql.QSqlQuery()
        query.setForwardOnly(True)
        where_stmt = ' AND '.join([
            '`{}` = ?'.format(x)
            for x in kwargs
            if x not in ['order_by', 'limit']
        ])
        where_stmt = 'WHERE ' + where_stmt if where_stmt else ''
        query.prepare("""
            SELECT {} FROM {} {} {} {}
        """.format(
            ', '.join([
                '`{}`'.format(x)
                for x in cls.ATTRIBUTES
            ]),
            cls.TABLE,
            where_stmt,
            'ORDER BY {}'.format(', '.join([
                '`{}`'.format(x)
                for x in kwargs['order_by']
            ]))
            if 'order_by' in kwargs else '',
            'LIMIT {}'.format(kwargs['limit'])
            if 'limit' in kwargs else '',
        ))
        for k, v in kwargs.items():
            if k not in ['order_by', 'limit']:
                query.addBindValue(v)
        query.exec()
        while query.next():
            res.append(cls.__create_from_value(query.value))
        return res

    @classmethod
    def create(cls, **kwargs):
        """Create new model in database.

        Args:
            **kwargs: Attributes of the model.

        Returns:
            Model: New model object.
        """
        res = cls(**kwargs)
        query = QtSql.QSqlQuery()
        query.setForwardOnly(True)
        query.prepare("""
            INSERT INTO `{}` {}
            VALUES ({})
        """.format(
            cls.TABLE,
            '({})'.format(
                ', '.join([
                    '`{}`'.format(x)
                    for x in kwargs
                ])
            ),
            ', '.join('?' * len(kwargs))
        ))
        for _, v in kwargs.items():
            query.addBindValue(v)
        if not query.exec():
            res = None
        else:
            if query.exec('SELECT last_insert_rowid()'):
                query.next()
                res.__dict__[res.PRIMARY_KEY[0]] = query.value(0)
            else:
                print(query.lastError().text())
        return res

    def __repr__(self) -> str:
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(
                '{}={}'.format(k, v)
                for k, v in self.__dict__.items()
                if k in self.ATTRIBUTES
            ),
        )
