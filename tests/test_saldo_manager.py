import unittest

from vlearn.controllers.auth import AuthController
from vlearn.controllers.saldo import SaldoManager
from vlearn.database import Database
from vlearn.models.pengguna import Pengguna


class TestSaldoManager(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)
        AuthController.register('John Doe', 'john@rpl.com', 'password', False)

    def test_saldo_manager(self):
        p = AuthController.get_user()
        # Test empty saldo
        s = SaldoManager.get_pengguna_saldo(p)
        self.assertEqual(s, 0, 'Should be 0')
        # Test add saldo and success
        saldo = 100
        SaldoManager.add_pengguna_saldo(p, saldo)
        s = SaldoManager.get_pengguna_saldo(p)
        self.assertEqual(s, saldo, 'Should be 100')
        # Test sub saldo and success
        saldo = 50
        SaldoManager.sub_pengguna_saldo(p, saldo)
        s = SaldoManager.get_pengguna_saldo(p)
        self.assertEqual(s, saldo, 'Should be 50')
    
    @classmethod
    def tearDownClass(self):
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()