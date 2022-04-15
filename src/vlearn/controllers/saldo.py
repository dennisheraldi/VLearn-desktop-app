""" Module for saldo manager """

from vlearn.models.pengguna import Pengguna


class SaldoManager:
    """Class for static saldo manager
    """
    @staticmethod
    def get_pengguna_saldo(pengguna:Pengguna) -> int:
        """Get pengguna saldo.

        Args:
            pengguna (Pengguna): Pengguna reference.

        Returns:
            int: Saldo value.
        """
        return pengguna.saldo

    @staticmethod
    def add_pengguna_saldo(pengguna:Pengguna, nilai_saldo:int):
        """Add pengguna saldo.

        Args:
            pengguna (Pengguna): Pengguna reference.
            nilai_saldo (int): Saldo value.

        Returns:
            int: Saldo value.
        """
        pengguna.saldo += nilai_saldo
        pengguna.save()

    @staticmethod
    def sub_pengguna_saldo(pengguna:Pengguna, nilai_saldo:int):
        """Substact pengguna saldo. Precondition: saldo >= nilai_saldo.

        Args:
            pengguna (Pengguna): Pengguna reference.
            nilai_saldo (int): Saldo value.

        Returns:
            int: Saldo value.
        """
        pengguna.saldo -= nilai_saldo
        pengguna.save()
