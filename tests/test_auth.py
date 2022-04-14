import unittest

from vlearn.controllers.auth import AuthController
from vlearn.database import Database
from vlearn.models.pengguna import Pengguna


class TestAuthController(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)

    def test_auth(self):
        # Test invalid login
        self.assertFalse(AuthController.is_logged_in(), 'Should not have user first.')
        self.assertFalse(AuthController.login('email', 'password'), 'Shouldn\'t found user.')
        self.assertFalse(AuthController.is_logged_in(), 'Should not logged in.')
        # Test valid register
        self.assertTrue(AuthController.register('Amar Fadil', 'amar@rpl.com', 'password', False), 'Should register user.')
        self.assertTrue(AuthController.is_logged_in(), 'Should logged in.')
        self.assertFalse(AuthController.is_user_admin(), 'Should not be admin.')
        p = AuthController.get_user()
        self.assertEqual(p.id_pengguna, 1, 'Should be user id 1.')
        self.assertEqual(p.nama, 'Amar Fadil', 'Should have correct name.')
        self.assertEqual(p.email, 'amar@rpl.com', 'Should have correct email.')
        AuthController.logout()
        self.assertFalse(AuthController.is_logged_in(), 'Should logged out.')
        # Test valid login
        self.assertTrue(AuthController.login('amar@rpl.com', 'password'), 'Should login user.')
        self.assertTrue(AuthController.is_logged_in(), 'Should logged in.')
        p = AuthController.get_user()
        self.assertEqual(p.id_pengguna, 1, 'Should be user id 1.')
        self.assertEqual(p.nama, 'Amar Fadil', 'Should have correct name.')
        self.assertEqual(p.email, 'amar@rpl.com', 'Should have correct email.')
        self.assertFalse(AuthController.is_user_admin(), 'Should not be admin.')
        AuthController.logout()
        self.assertFalse(AuthController.is_logged_in(), 'Should logged out.')
        # Test valid register admin
        self.assertTrue(AuthController.register('Admin', 'admin@rpl.com', 'admin123', True), 'Should register admin.')
        self.assertTrue(AuthController.is_logged_in(), 'Should logged in.')
        self.assertTrue(AuthController.is_user_admin(), 'Should be admin.')
        p = AuthController.get_user()
        self.assertEqual(p.id_pengguna, 2, 'Should be user id 2.')
        self.assertEqual(p.nama, 'Admin', 'Should have correct name.')
        self.assertEqual(p.email, 'admin@rpl.com', 'Should have correct email.')
        AuthController.logout()
        self.assertFalse(AuthController.is_logged_in(), 'Should logged out.')
        # Test valid login admin
        self.assertTrue(AuthController.login('admin@rpl.com', 'admin123'), 'Should login admin.')
        self.assertTrue(AuthController.is_logged_in(), 'Should logged in.')
        p = AuthController.get_user()
        self.assertEqual(p.id_pengguna, 2, 'Should be user id 2.')
        self.assertEqual(p.nama, 'Admin', 'Should have correct name.')
        self.assertEqual(p.email, 'admin@rpl.com', 'Should have correct email.')
        self.assertTrue(AuthController.is_user_admin(), 'Should be admin.')
        AuthController.logout()
        # Test invalid login
        self.assertFalse(AuthController.login('test', 'test'), 'Shouldn\'t found user.')
        # Test user exist register
        self.assertFalse(AuthController.register('Amar', 'amar@rpl.com', 'password', False), 'Shouldn\'t register user.')
        
        
    @classmethod
    def tearDownClass(self):
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()
