import unittest

from vlearn.controllers.course import CoursePengguna
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.seeder import Seeder
from vlearn.models.tanggapan import Tanggapan


class TestSaldoManager(unittest.TestCase):
    seed = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.seed = Seeder(':memory:')
        cls.seed.seed_all()

    def test_seed(self):
        self.assertEqual(len(Pengguna.all()), 100)
        self.assertEqual(len(Course.all()), 100)
        self.assertEqual(len(Review.all()), 1000)
        self.assertEqual(len(Tanggapan.all()), 1000)
        self.assertEqual(len(CoursePengguna.all()), 100*99//2)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.seed

if __name__ == '__main__': # pragma: no cover
    unittest.main()