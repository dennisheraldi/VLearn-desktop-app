import unittest

from vlearn.database import Database
from vlearn.models.pengguna import Pengguna


class TestPenggunaModel(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)
        
    def test_pengguna_crud(self):
        # Create
        p = Pengguna.create(
            nama='nama',
            email='email',
            password='password',
            role='user'
        )
        self.assertIsNotNone(p.id_pengguna, 'id_pengguna should not be None')
        self.assertEqual(p.nama, 'nama')
        self.assertEqual(p.email, 'email')
        self.assertEqual(p.password, 'password')
        self.assertEqual(p.role, 'user')
        self.assertEqual(p.saldo, 0)
        self.assertIsNone(p.session_id, 'Pengguna session_id should be None for now')
        
        # Read/Index
        p = Pengguna.get(email='email')
        self.assertIsNotNone(p, 'Pengguna should available')
        self.assertEqual(p.nama, 'nama')
        self.assertEqual(p.email, 'email')
        self.assertEqual(p.password, 'password')
        self.assertEqual(p.role, 'user')
        self.assertEqual(p.saldo, 0)
        self.assertEqual(p.session_id, '', 'Pengguna session_id should be None for now')
        
        # Get/All
        Pengguna.create(
            nama='nama2',
            email='email2',
            password='password2',
            role='admin',
            saldo=10000,
            session_id='mock_session_id2'
        )
        p = Pengguna.all(order_by=['id_pengguna'], limit=2)
        self.assertEqual(len(p), 2, '2 Pengguna should exist')
        self.assertEqual(p[0].nama, 'nama')
        self.assertEqual(p[1].id_pengguna, 2)
        self.assertEqual(p[1].nama, 'nama2')
        self.assertEqual(p[1].email, 'email2')
        self.assertEqual(p[1].password, 'password2')
        self.assertEqual(p[1].role, 'admin')
        self.assertEqual(p[1].saldo, 10000)
        self.assertEqual(p[1].session_id, 'mock_session_id2')
        Pengguna.get(id_pengguna=2).delete()
        
        # Update
        p = Pengguna.get(email='email')
        p.email = 'email_baru'
        if p.save():
            p = Pengguna.get(email='email_baru')
            self.assertIsNotNone(p, 'Pengguna email should be changed to email_baru.')
            p = Pengguna.get(email='email')
            self.assertIsNone(p, 'Pengguna email should not exist.')

        
    @classmethod
    def tearDownClass(self):
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()
