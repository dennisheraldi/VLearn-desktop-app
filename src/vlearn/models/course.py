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

