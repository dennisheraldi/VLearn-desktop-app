import os
from database import Database
from views.display import DisplayManager

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
    print("Hello")
    # Tampilan menu utama
    # DisplayManager()