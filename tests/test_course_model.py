import unittest

from vlearn.database import Database
from vlearn.models.course import Course


class TestCourseModel(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Course.CREATE_QUERY)

    def test_course_crud(self):
        # Create
        c = Course.create(
            judul='judul',
            deskripsi='deskripsi',
            harga=1,
            link_video='link_video',
            durasi=1
        )
        self.assertIsNotNone(c.id_course, 'id_course should not be None')
        self.assertEqual(c.judul, 'judul')
        self.assertEqual(c.deskripsi, 'deskripsi')
        self.assertEqual(c.harga, 1)
        self.assertEqual(c.link_video, 'link_video')
        self.assertEqual(c.durasi, 1)
        # Read/Index
        c = Course.get(judul='judul')
        self.assertIsNotNone(c, 'Course should available')
        self.assertEqual(c.judul, 'judul')
        self.assertEqual(c.deskripsi, 'deskripsi')
        self.assertEqual(c.harga, 1)
        self.assertEqual(c.link_video, 'link_video')
        self.assertEqual(c.durasi, 1)
        # Get/All
        Course.create(
            judul='judul2',
            deskripsi='deskripsi2',
            harga=2, 
            link_video='link_video2',
            durasi=2
        )
        c = Course.all(order_by=['id_course'], limit=2)
        self.assertEqual(len(c), 2, '2 Course should exist')
        self.assertEqual(c[0].judul, 'judul')
        self.assertEqual(c[1].id_course, 2)
        Course.get(id_course=2).delete()
        # Update
        c = Course.get(judul='judul')
        c.judul = 'judul_baru'
        c.save()
        c = Course.get(judul='judul_baru')
        self.assertIsNotNone(c, 'Course judul should be changed to judul_baru.')
        c = Course.get(judul='judul')
        self.assertIsNone(c, 'Course judul should not exist.')
        # Delete
        c = Course.get(judul='judul_baru')
        self.assertIsNotNone(c, 'Course judul_baru should exist.')
        c.delete()
        c = Course.get(judul='judul_baru')
        self.assertIsNone(c, 'Course judul_baru should be deleted.')
        c = Course.get(judul='judul')
        self.assertIsNone(c, 'Course judul should not exist.')
    
    @classmethod
    def tearDownClass(self) -> None:
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover
    unittest.main()