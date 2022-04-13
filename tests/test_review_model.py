import unittest

from vlearn.database import Database
from vlearn.models.review import Review


class TestReviewModel(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        Database.create_connection(':memory:')
        Database.create_table(Review.CREATE_QUERY)

    def test_review_crud(self):
        # Create
        r = Review.create(
            isi_review='isi_review'
        )
        self.assertIsNotNone(r.id_review, 'id_review should not be None')
        self.assertEqual(r.isi_review, 'isi_review')
        # Read/Index
        r = Review.get(isi_review='isi_review')
        self.assertIsNotNone(r, 'Review should available')
        self.assertEqual(r.isi_review, 'isi_review')
        # Get/All
        Review.create(
            isi_review='isi_review2'
        )
        r = Review.all(order_by=['id_review'], limit=2)
        self.assertEqual(len(r), 2, '2 Review should exist')
        self.assertEqual(r[0].isi_review, 'isi_review')
        Review.get(id_review=2).delete()
        # Update
        r = Review.get(isi_review='isi_review')
        r.isi_review = 'isi_review_baru'
        r.save()
        r = Review.get(isi_review='isi_review_baru')
        self.assertIsNotNone(r, 'Review isi_review should be changed to isi_review_baru.')
        r = Review.get(isi_review='isi_review')
        self.assertIsNone(r, 'Review isi_review should not exist.')
        # Delete
        r = Review.get(isi_review='isi_review_baru')
        self.assertIsNotNone(r, 'Review isi_review_baru should exist.')
        r.delete()
        r = Review.get(isi_review='isi_review_baru')
        self.assertIsNone(r, 'Review isi_review_baru should be deleted.')
        r = Review.get(isi_review='isi_review')
        self.assertIsNone(r, 'Review isi_review should not exist.')


    @classmethod
    def tearDownClass(self) -> None:
        Database.close_connection()

if __name__ == '__main__': # pragma: no cover 
    unittest.main()
