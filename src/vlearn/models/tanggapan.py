"""Module implementation of tanggapan blueprints model.
"""
from vlearn.models.base import Model


class Tanggapan(Model):
    """Base class for tanggapan model.
    """
    TABLE = 'tanggapan'
    AUTOINCREMENT = False
    CREATE_QUERY = """
        CREATE TABLE IF NOT EXISTS `tanggapan` (
            `id_review` INTEGER NOT NULL,
            `id_pengguna` INTEGER NOT NULL,
            `id_course` INTEGER NOT NULL,
            `nilai_rating` REAL NOT NULL,
            PRIMARY KEY (`id_review`, `id_pengguna`, `id_course`),
            FOREIGN KEY (`id_review`) REFERENCES review(`id_review`),
            FOREIGN KEY (`id_pengguna`) REFERENCES pengguna(`id_pengguna`),
            FOREIGN KEY (`id_course`) REFERENCES courses(`id_course`)
        );
    """

    PRIMARY_KEY = ['id_review', 'id_pengguna', 'id_course']
    ATTRIBUTES = ['id_review', 'id_pengguna', 'id_course', 'nilai_rating']

    def __init__(self,
        id_review:int,
        id_pengguna:int,
        id_course:int,
        nilai_rating:float
    ):
        self.id_review = id_review
        self.id_pengguna = id_pengguna
        self.id_course = id_course
        self.nilai_rating = nilai_rating
        super().__init__()
