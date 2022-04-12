import unittest

from PyQt5.QtSql import QSqlError

from vlearn.database import Database


class TestDatabase(unittest.TestCase):
    def test_invalid_connection(self):
        self.assertFalse(Database.create_connection('db/db\\.db'), 'Database should not be created.')
        self.assertFalse(Database.create_table('SELECT FROM'), 'Should be any error')

if __name__ == '__main__': # pragma: no cover
    unittest.main()