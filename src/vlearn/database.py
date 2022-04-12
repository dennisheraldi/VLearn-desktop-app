"""Module for static database methods."""
from PyQt5 import QtSql


class Database:
    """Class for static database methods."""
    @staticmethod
    def create_connection(db_file):
        """Buat koneksi ke database SQLite.
        Koneksi ada di database.conn

        Args:
            db_file (str): Path ke file database
        """
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_file)

        return db.open()

    @staticmethod
    def create_table(create_table_sql):
        """Buat tabel di database, jika belum dibuat

        Args:
            create_table_sql ([type]): SQL Query untuk membuat tabel
        """
        query = QtSql.QSqlQuery()
        query.exec(create_table_sql)
        return query.lastError() is None


    @staticmethod
    def close_connection():
        """Tutup koneksi ke database"""
        db = QtSql.QSqlDatabase.database()
        db.close()
