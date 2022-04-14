import unittest

from vlearn.controllers.auth import AuthController
from vlearn.controllers.course import CourseManager, CoursePengguna
from vlearn.controllers.tanggapan import TanggapanManager
from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.tanggapan import Tanggapan


class TestTanggapanManager(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)
        Database.create_table(Course.CREATE_QUERY)
        Database.create_table(CoursePengguna.CREATE_QUERY)
        Database.create_table(Tanggapan.CREATE_QUERY)
        Database.create_table(Review.CREATE_QUERY)
        AuthController.register('Amar Fadil', 'amar@rpl.com', 'password', False)
        for i in range(5):
            Course.create(
                judul=f'judul{i}',
                deskripsi='deskripsi',
                harga=i,
                link_video='',
                durasi=i*10,
            )

    def test_tanggapan_manager(self):
        p = AuthController.get_user()
        c = Course.get(id_course=1)
        CourseManager.add_course_pengguna(c, p)
        # Test get course pengguna
        t, _ = TanggapanManager.get_course_tanggapan(c)
        self.assertEqual(len(t), 0, 'Should have no tanggapan')
        # Test add tanggapan
        self.assertIsNotNone(TanggapanManager.add_course_tanggapan(c, p, 5.0, 'Sangat bagus'), 'Should add tanggapan')
        self.assertIsNotNone(TanggapanManager.add_course_tanggapan(c, p, 3.5, 'Agak kurang'), 'Should add tanggapan')
        # Test get tanggapan course
        t, avg_rating = TanggapanManager.get_course_tanggapan(c)
        self.assertEqual(len(t), 2, 'Should have 2 tanggapan')
        self.assertIsNotNone(t[0].review, 'Should have review')
        self.assertIsNotNone(t[1].review, 'Should have review')
        self.assertAlmostEqual(t[0].nilai_rating, 5.0, 'Should have rating 5.0')
        self.assertAlmostEqual(t[1].nilai_rating, 3.5, 'Should have rating 3.5')
        self.assertEqual(t[0].review.isi_review, 'Sangat bagus', 'Should have review isi_review')
        self.assertEqual(t[1].review.isi_review, 'Agak kurang', 'Should have review isi_review')
        self.assertAlmostEqual(avg_rating, 4.25, 'Should have avg rating 4.25')
        # Get all course and tanggapan
        c = Course.all(order_by=['id_course'])
        TanggapanManager.add_course_tanggapan(c[1], p, 5.0, 'Sangat bagus')
        TanggapanManager.add_course_tanggapan(c[2], p, 4.0, 'Lumayan bagus')
        TanggapanManager.add_course_tanggapan(c[3], p, 3.0, 'Agak kurang')
        t = TanggapanManager.get_courses_tanggapan(c)
        self.assertEqual(len(t[0].tanggapan), 2, 'Should have 2 tanggapan')
        for i in range(1, 4):
            self.assertEqual(len(t[i].tanggapan), 1, 'Should have 1 tanggapan')
            self.assertAlmostEqual(t[i].avg_rating, 6.0 - i, 'Should have correct avg rating')
            self.assertEqual(t[i].tanggapan[0].review.isi_review,
                {1: 'Sangat bagus', 2: 'Lumayan bagus', 3: 'Agak kurang'}[i]
            , 'Should have correct isi_review')
        self.assertEqual(len(t[4].tanggapan), 0, 'Should have 0 tanggapan')
        self.assertAlmostEqual(t[4].avg_rating, 0.0, 'Should have avg rating 0.0')
        
        
    @classmethod
    def tearDownClass(self):
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()