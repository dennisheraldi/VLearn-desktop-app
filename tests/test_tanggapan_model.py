import unittest

from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.tanggapan import Tanggapan


class TestTanggapanModel(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Tanggapan.CREATE_QUERY)
        Database.create_table(Review.CREATE_QUERY)
        Database.create_table(Pengguna.CREATE_QUERY)
        Database.create_table(Course.CREATE_QUERY)
        
        for _ in range(2):
            Course.create(
                judul='judul',
                deskripsi='deskripsi',
                harga=1,
                link_video='link_video',
                durasi=1
            )
            Review.create(
                isi_review='isi_review'
            )
            Pengguna.create(
                nama='nama',
                email='email',
                password='password',
                role='user'
            )

    
    def test_tanggapan_crud(self):
        # Create
        t = Tanggapan.create(
            id_review=1,
            id_pengguna=1,
            id_course=1,
            nilai_rating=1.0
        )
        print(t)
        self.assertIsNotNone(t.id_review, 'id_review should not be None')
        self.assertIsNotNone(t.id_pengguna, 'id_pengguna should not be None')
        self.assertIsNotNone(t.id_course, 'id_course should not be None')
        self.assertEqual(t.nilai_rating, 1.0)
        # Read/Index
        t = Tanggapan.get(id_review=1, id_pengguna=1, id_course=1)
        self.assertIsNotNone(t, 'id_pengguna should available')
        self.assertIsNotNone(t, 'id_pengguna should available')
        self.assertIsNotNone(t, 'id_course should available')
        self.assertEqual(t.nilai_rating, 1.0)
        # Get/All
        Tanggapan.create(
            id_review=2,
            id_pengguna=2,
            id_course=2,
            nilai_rating=2.0
        )
        t = Tanggapan.all(order_by=['id_review'], limit=2)
        self.assertEqual(len(t), 2, '2 Tanggapan should exist')
        self.assertEqual(t[0].id_review, 1)
        self.assertEqual(t[1].id_review, 2)
        Tanggapan.get(id_review=2).delete()
        # Update
        t = Tanggapan.get(nilai_rating=1.0)
        t.nilai_rating = 5.0
        t.save()
        t = Tanggapan.get(nilai_rating=5.0)
        self.assertIsNotNone(t, 'Tanggapan nilai_rating should be changed to 5.0.')
        t = Tanggapan.get(nilai_rating=1.0)
        self.assertIsNone(t, 'Tanggapan nilai_rating should not exist.')
        # Delete
        t = Tanggapan.get(nilai_rating=5.0)
        self.assertIsNotNone(t, 'Tanggapan nilai_rating should exist.')
        t.delete()
        t = Tanggapan.get(nilai_rating=5.0)
        self.assertIsNone(t, 'Tanggapan id_review should be deleted.')
        t = Tanggapan.get(nilai_rating=1.0)
        self.assertIsNone(t, 'Tanggapan nilai_rating should not exist.')
        
    @classmethod
    def tearDownClass(self) -> None:
        Database.close_connection()

if __name__ == 'main' : #pragma: no cover
    unittest.main()