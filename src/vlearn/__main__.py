"""Main driver for application client module.
"""

import os

from vlearn.controllers.course import CoursePengguna
from vlearn.database import Database
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.tanggapan import Tanggapan
from vlearn.views.display import DisplayManager

if __name__ == '__main__':
    # Dapatkan direktori sekarang
    current_dir = os.getcwd()
    # Dapatkan path ke file database
    database_path = os.path.join(current_dir, 'db', 'database.db')

    # Cek apakah ada folder `db` di direktori sekarang
    if not os.path.exists('db'):
        # Buat folder `db` di direktori sekarang
        os.makedirs('db')
    # Buat koneksi ke database
    Database.create_connection(database_path)
    # Buat tabel jika belum ada
    for i in [Course, Pengguna, Review, Tanggapan, CoursePengguna]:
        Database.create_table(i.CREATE_QUERY)
    # Tampilan menu utama
    DisplayManager()
