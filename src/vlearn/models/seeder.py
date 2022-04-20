"""Seeder module.
"""
import datetime
import random

from faker import Faker

from vlearn.controllers.course import CoursePengguna
from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.tanggapan import Tanggapan


class Seeder:
    """Base class for seeder.
    """

    def __init__(self, database_path):
        # Buat koneksi ke database
        Database.create_connection(database_path)
        # Buat tabel jika belum ada
        for i in [Course, Pengguna, Review, Tanggapan, CoursePengguna]:
            Database.create_table(i.CREATE_QUERY)
        self.fake = Faker()
        self.pengguna_id = []
        self.course_id = []
        self.review_id = []

    def seed_pengguna(self):
        """Seed pengguna.
        """
        for _ in range(100):
            p = Pengguna.create(
                nama=self.fake.name(),
                email=self.fake.email(),
                password=self.fake.password(),
                role='user',
                saldo=self.fake.random_int(min=0, max=1000000),
            )
            self.pengguna_id.append(p.id_pengguna)

    def seed_course(self):
        """Seed courses.
        """
        for _ in range(100):
            c = Course.create(
                judul=self.fake.sentence(),
                deskripsi=self.fake.text(),
                harga=self.fake.random_int(min=0, max=1000000),
                link_video=self.fake.url(),
                durasi=self.fake.random_int(min=0, max=100),
            )
            self.course_id.append(c.id_course)

    def seed_review(self):
        """Seed review.
        """
        for _ in range(1000):
            r = Review.create(
                isi_review=self.fake.text(),
            )
            self.review_id.append(r.id_review)

    def seed_tanggapan(self):
        """Seed tanggapan.
        """
        for i in range(1000):
            Tanggapan.create(
                id_review=self.review_id[i],
                id_pengguna=self.fake.random_element(self.pengguna_id),
                id_course=self.fake.random_element(self.course_id),
                nilai_rating=round(random.uniform(0, 5), 2),
            )

    def seed_course_pengguna(self):
        """Seed course pengguna.
        """
        fake_uniq = Faker()
        self.fake.unique.clear()
        for v in self.pengguna_id:
            N = self.fake.unique.random_int(min=0, max=99)
            fake_uniq.unique.clear()
            for _ in range(N):
                rand_time = self.fake.date_time_between(
                    start_date='-5y', end_date='now')

                CoursePengguna.create(
                    id_pengguna=v,
                    id_course=self.course_id[fake_uniq.unique.random_int(
                        min=0, max=99)],
                    waktu_pembelian=datetime.datetime.timestamp(rand_time),
                )

    def seed_all(self):
        """Seed all.
        """
        self.seed_pengguna()
        self.seed_course()
        self.seed_review()
        self.seed_tanggapan()
        self.seed_course_pengguna()

    def __del__(self):
        Database.close_connection()


if __name__ == '__main__':  # pragma: no cover
    Seeder('db/database.db').seed_all()
