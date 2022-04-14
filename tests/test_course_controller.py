import unittest

from vlearn.controllers.auth import AuthController
from vlearn.controllers.course import CourseManager, CoursePengguna
from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna


class TestCourseManager(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Pengguna.CREATE_QUERY)
        Database.create_table(Course.CREATE_QUERY)
        Database.create_table(CoursePengguna.CREATE_QUERY)
        AuthController.register('Amar Fadil', 'amar@rpl.com', 'password', False)
        for i in range(4):
            Course.create(
                judul=f'judul{i}',
                deskripsi='deskripsi',
                harga=i,
                link_video='',
                durasi=i*10,
            )

    def test_course_manager(self):
        p = AuthController.get_user()
        # Test empty course pengguna
        c = CourseManager.get_courses_pengguna(p)
        self.assertEqual(len(c), 0, 'Should be empty.')
        # Test add course and success
        c = Course.get(id_course=1)
        self.assertIsNotNone(CourseManager.add_course_pengguna(c, p), 'Should add course')
        # Test get course pengguna
        c = CourseManager.get_courses_pengguna(p)
        self.assertEqual(len(c), 1, 'User should have only 1 course')
        self.assertEqual(c[0].id_course, 1, 'Should be course id 1')
        
        
    @classmethod
    def tearDownClass(self):
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()
