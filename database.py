from PyQt5 import QtSql

class Database(object):

    @staticmethod
    def create_connection(db_file):
        """Buat koneksi ke database SQLite.
        Koneksi ada di database.conn

        Args:
            db_file (str): Path ke file database
        """
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_file)

        if not db.open():
            # Terjadi error dalam mengakses database
            print("Error ketika membuka database!")
            exit()

    @staticmethod
    def create_table(create_table_sql):
        """Buat tabel di database, jika belum dibuat

        Args:
            create_table_sql ([type]): SQL Query untuk membuat tabel
        """
        try:
            c = QtSql.QSqlQuery()
            c.exec(create_table_sql)
        except QtSql.QSqlError as e:
            print(e)
