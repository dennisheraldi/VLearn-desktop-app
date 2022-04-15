import unittest

from vlearn.controllers.auth import AuthController
from vlearn.controllers.course import CoursePengguna
from vlearn.controllers.pembelian_course import PembelianCourseController
from vlearn.controllers.saldo import SaldoManager
from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna


class TestPembelianCourseController(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)
        Database.create_table(Course.CREATE_QUERY)
        Database.create_table(CoursePengguna.CREATE_QUERY)

        AuthController.register(
            'Amar Fadil', 'malikakbar@rpl.com', 'password', False)

        for i in range(5):
            Course.create(
                judul=f"judul course {i+1}",
                deskripsi=f"ini deskripsi course {i+1}",
                harga=((i+1)*20000),
                link_video=f"ini link course {i+1}",
                durasi=i*20
            )

    def test_pembelian_course(self):
        p = AuthController.get_user()
        first_saldo = 100000
        SaldoManager.add_pengguna_saldo(p, first_saldo)

        courses = Course.all()

        self.assertTrue(PembelianCourseController.beli_course(
            p, courses[0]), "Should be able to buy course")
        
        self.assertEqual(SaldoManager.get_pengguna_saldo(p), first_saldo - courses[0].harga, "Should be able to buy course")
        
        self.assertTrue(PembelianCourseController.beli_course(p, courses[1]), "Should be able to buy course")
        
        for i in range(2, len(courses)):
            self.assertFalse(PembelianCourseController.beli_course(p, courses[i]), "Should not be able to buy course")
        
        self.assertEqual(SaldoManager.get_pengguna_saldo(p), first_saldo - courses[0].harga - courses[1].harga, "Balance should not be substracted if fail to buy")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
