"""Module implementation of course blueprints model.
"""
from vlearn.models.base import Model


class Course(Model):
    """Base class for course model.
    """
    TABLE = 'courses'
    CREATE_QUERY = """
        CREATE TABLE IF NOT EXISTS `courses` (
            `id_course` INTEGER PRIMARY KEY AUTOINCREMENT,
            `judul` VARCHAR(255) NOT NULL,
            `deskripsi` VARCHAR(2000) NOT NULL,
            `harga` INTEGER NOT NULL,
            `link_video` VARCHAR(255) NOT NULL,
            `durasi` INTEGER NOT NULL
        );
    """
    PRIMARY_KEY = ['id_course']
    ATTRIBUTES = ['judul', 'deskripsi', 'harga', 'link_video', 'durasi', 'id_course']

    def __init__(self,
        judul:str, deskripsi:str,
        harga:int, link_video:str,
        durasi:int, id_course:int=None
    ):
        self.judul = judul
        self.deskripsi = deskripsi
        self.harga = harga
        self.link_video = link_video
        self.durasi = durasi
        self.id_course = id_course
        super().__init__()

if __name__ == '__main__': # pragma: no cover
    import sys

    from PyQt5 import QtSql
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('db/database.db')
    if not db.open():
        print('error')
        sys.exit()
    db.exec(Course.CREATE_QUERY)
    if db.lastError().text() == '':
        c = Course.create(
            judul='judul',
            deskripsi='deskripsi',
            harga=1,
            link_video='link_video',
            durasi=1
        )
        if c.delete():
            print(c)
    else:
        print(db.lastError().text())
