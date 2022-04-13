"""Module implementation of pengguna model.
"""

from vlearn.models.base import Model


class Pengguna(Model):
    """Class for pengguna model
    """

    TABLE = 'pengguna'
    CREATE_QUERY = """
        CREATE TABLE IF NOT EXISTS `pengguna` (
            `id_pengguna` INTEGER PRIMARY KEY AUTOINCREMENT,
            `nama` VARCHAR(255) NOT NULL,
            `email` VARCHAR(255) NOT NULL,
            `password` VARCHAR(255) NOT NULL,
            `role` VARCHAR(255) NOT NULL,
            `saldo` INTEGER NOT NULL,
            `session_id` VARCHAR(255)
        );
    """
    PRIMARY_KEY = ['id_pengguna']
    ATTRIBUTES = ['nama', 'email', 'password', 'role', 'saldo', 'session_id', 'id_pengguna']

    def __init__(
        self, nama: str, email: str, password: str, role: str,
        saldo: int = 0, session_id: str = None, id_pengguna: int = None
    ):
        self.nama = nama
        self.email = email
        self.password = password
        self.role = role
        self.saldo = saldo
        self.session_id = session_id
        self.id_pengguna = id_pengguna
        super().__init__()
