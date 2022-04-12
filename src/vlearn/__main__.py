"""Main driver for application client module.
"""

import os

from vlearn.database import Database
# from vlearn.views.display import DisplayManager
from vlearn.models.course import Course

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
    for x in [Course]:
        Database.create_table(x.CREATE_QUERY)
    print('Hello')
    # Tampilan menu utama
    # DisplayManager()
