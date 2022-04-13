"""Module implementation of course blueprints model.
"""
from vlearn.models.base import Model


class Review(Model):
    """Base class for course Review.
    """
    TABLE = 'review'
    CREATE_QUERY = """
        CREATE TABLE IF NOT EXISTS `review` (
            `id_review` INTEGER PRIMARY KEY AUTOINCREMENT,
            `isi_review` VARCHAR(2000) NOT NULL
        );
    """
    PRIMARY_KEY = ['id_review']
    ATTRIBUTES = ['isi_review', 'id_review']

    def __init__(self,
        isi_review:str, id_review:int=None
    ):
        self.isi_review = isi_review
        self.id_review = id_review
        super().__init__()
