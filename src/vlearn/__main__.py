"""Main driver for application client module.
"""

import os

from vlearn.models.seeder import Seeder
from vlearn.views.auth_display import ViewAuth
from vlearn.views.beri_tanggapan_display import ViewBeriTanggapan
from vlearn.views.detail_course_display import ViewDetailCourse
from vlearn.views.display import DisplayManager
from vlearn.views.isi_saldo_display import IsiSaldoDisplay
from vlearn.views.list_course_display import ListCourseDisplay

if __name__ == '__main__':
    # Dapatkan direktori sekarang
    current_dir = os.getcwd()
    # Dapatkan path ke file database
    database_path = os.path.join(current_dir, 'db', 'database.db')

    # Cek apakah ada folder `db` di direktori sekarang
    if not os.path.exists('db'):
        # Buat folder `db` di direktori sekarang
        os.makedirs('db')
    # Buat koneksi ke database dan buat tabel jika belum ada
    seeder = Seeder(database_path)
    # Tampilan menu utama
    DisplayManager({
        'auth.login': ViewAuth.Login,
        'auth.register': ViewAuth.Register,
        'list_course': ListCourseDisplay,
        'detail_course': ViewDetailCourse,
        'beri_tanggapan': ViewBeriTanggapan,
        'isi_saldo': IsiSaldoDisplay
    })
