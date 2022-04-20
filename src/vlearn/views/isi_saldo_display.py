'''Module implementation of isi saldo view.
'''

import locale

from vlearn.controllers.auth import AuthController
from vlearn.controllers.saldo import SaldoManager
from vlearn.views.display import AppDisplay, DisplayManager
from vlearn.views.ui.isi_saldo import Ui_MainWindow as Ui_IsiSaldo


class IsiSaldoDisplay(AppDisplay):
    '''
    View untuk isi saldo
    '''
    def __init__(self):
        '''
        Buat view menu utama isi saldo.
        '''
        # UI setup
        super().__init__(Ui_IsiSaldo)

        self.p = AuthController.get_user()
        saldo_value = SaldoManager.get_pengguna_saldo(self.p)

        locale.setlocale(locale.LC_ALL, "")
        self.window.tf_saldo.setText(
            locale.currency(saldo_value, grouping=True)
        ) # Menampilkan saldo sekarang

        # Callback
        self.window.btn_pay.clicked.connect(self.pay) # Jika menekan tombol bayar

        self.window.btn_cancel.mousePressEvent = \
                lambda _: DisplayManager.ins().show("list_course")

    def pay(self):
        '''
        Melakukan pembayaran untuk mengisi saldo.
        '''
        add_saldo = self.window.if_saldo_add.text() # Menerima Inputan saldo yang akan ditambahkan
        try:
            if add_saldo == "":
                DisplayManager.ins().show_error("Error", "Masukan saldo yang valid")
            else:
                add_saldo = int(add_saldo)
                if add_saldo <= 0:
                    DisplayManager.ins().show_error("Error", "Masukan saldo yang valid")
                else:
                    SaldoManager.add_pengguna_saldo(self.p, add_saldo)
                    DisplayManager.ins().show_success("Success", "Saldo berhasil ditambahkan")
                    DisplayManager.ins().show("isi_saldo")
        except ValueError:
            DisplayManager.ins().show_error("Error", "Saldo harus berupa angka")
