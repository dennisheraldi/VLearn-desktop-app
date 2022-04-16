"""Module for display base class and manager."""
import sys

from PyQt5 import QtWidgets


class AppDisplay(QtWidgets.QMainWindow):
    """Base class for every views.
    """
    def __init__(self, user_interface: object):
        """
        Buat View baru untuk diregister ke UIManager

        Args:
            ui: Kode python UI QtDesigner yang digenerate dari pyuic5 (.ui)
        """
        super().__init__()
        self.window = user_interface()
        self.window.setupUi(self)
        self.setWindowTitle(f'{self.windowTitle()} - VLearn')
        self.setFixedSize(self.size())


class DisplayManager:
    """Display manager."""
    __instance = None

    @staticmethod
    def ins():
        """
        Mendapatkan instance UIManager yang bisa dipanggil di class lain
        Returns:
            UIManager: instance UIManager
        """
        return DisplayManager.__instance

    def __init__(self, displays: dict):
        """
        Membuat instance baru dari UIManager
        """
        # Inisialisasi UIManager
        if DisplayManager.__instance is None:
            DisplayManager.__instance = self
        # Import semua views

        # Buat instance QApplication baru
        self.app = QtWidgets.QApplication(sys.argv)

        # Register semua fungsi pembuat window beserta routenya
        self.windows = displays
        # Window utama adalah `auth.login`
        self.current_window : AppDisplay  = self.windows['auth.login']()
        # # Tampilkan window utama
        self.current_window.show()
        # Program exit dengan error kode dari QApplication
        sys.exit(self.app.exec_())

    def show(self, window_name, **kwargs):
        """
        Fungsi untuk menampilkan window dengan routenya

        Args:
            window_name (str): Route window yang ingin ditampilkan
            **kwargs: Argumen lain untuk custom show method
        """
        self.current_window.close()
        self.current_window = self.windows[window_name](**kwargs)
        self.current_window.show()

    def show_main(self):
        """
        Fungsi untuk menampilkan menu utama
        """
        self.show('main')

    @staticmethod
    def get_message_box(icon, title, message, info='', buttons=QtWidgets.QMessageBox.Ok):
        """
        Dapatkan instance QMessageBox untuk ditampilkan ke user

        Args:
            icon (QtWidgets.QMessageBox.Icon): Icon dari messagebox
            title (str): Judul dari messagebox
            message (str): Pesan utama yang disampaikan di messagebox
            info (str): Pesan
            buttons: Button yang tersedia di messagebox

        Returns:
            QtWidgets.MessageBox: Instance QMessageBox baru
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        if info:
            msg.setInformativeText(info)
        msg.setStandardButtons(buttons)
        return msg

    @staticmethod
    def show_error(title, message, info=''):
        """
        Menampilkan pesan error ke user

        Args:
            title (str): Judul dari messagebox
            message (str): Pesan yang akan disampaikan ke messagebox
            info (str): Pesan tambahan yang ditampilkan ke messagebox
        """
        msg = DisplayManager.get_message_box(QtWidgets.QMessageBox.Critical, title, message, info)
        msg.exec()

    @staticmethod
    def show_confirm(title, message, yes_call, info=''):
        """
        Menampilkan pesan konfirmasi ke user dan panggil `yes_call` jika user menekan tombol Yes

        Args:
            title (str): Judul dari messagebox
            message (str): Pesan yang akan disampaikan ke messagebox
            yes_call: Fungsi/lambda yang akan dipanggil ketika tombol yes ditekan
            info (str): Pesan tambahan yang ditampilkan ke messagebox
        """
        msg = DisplayManager.get_message_box(QtWidgets.QMessageBox.Question, title, message, info,
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg.exec() == QtWidgets.QMessageBox.Yes:
            yes_call()

    @staticmethod
    def show_success(title, message, ok_call=None, info=''):
        """
        Menampilkan pesan sukses ke user dan panggil `ok_call` jika user menekan tombol Ok

        Args:
            title (str): Judul dari messagebox
            message (str): Pesan yang akan disampaikan ke messagebox
            ok_call: Fungsi/lambda yang akan dipanggil ketika tombol Ok ditekan
            info (str): Pesan tambahan yang ditampilkan ke messagebox
        """
        msg = DisplayManager.get_message_box(
            QtWidgets.QMessageBox.Information,
            title,
            message,
            info,
        )
        if msg.exec() == QtWidgets.QMessageBox.Ok and ok_call is not None:
            ok_call()
