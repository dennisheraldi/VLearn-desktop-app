'''Module implementation of detail course display view.
'''

import locale
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets

from vlearn.controllers.auth import AuthController
from vlearn.controllers.course import Course, CoursePengguna
from vlearn.controllers.tanggapan import TanggapanManager
from vlearn.views.display import AppDisplay, DisplayManager
from vlearn.views.ui.detail_course import Ui_MainWindow as Ui_DetailCourse


class ViewDetailCourse(AppDisplay):
    '''
    View untuk detail course
    '''

    def __init__(self, course_id):
        '''
        Buat view detail course
        '''
        super().__init__(Ui_DetailCourse)

        self.i = 0

        self.course_data = Course.get(id_course=course_id)

        is_sudah_beli = CoursePengguna.get(id_course = course_id,
            id_pengguna = AuthController.get_user().id_pengguna) is not None

        locale.setlocale(locale.LC_ALL, "")
        self.window.label_nama_course.setText(self.course_data.judul)
        self.window.label_deskripsi_course.setText(self.course_data.deskripsi)
        self.window.label_harga_course.setText(
            locale.currency(self.course_data.harga, grouping=True)
        )

        self.window.label_saldo.setText(
            "Saldo: " + locale.currency(
                AuthController.get_user().saldo, grouping=True
            )
        )

        self.window.img_course.setPixmap(
            QtGui.QPixmap.fromImage(
                QtGui.QImage(
                    r"src\vlearn\views\ui\img\course_img.png")))
        self.window.img_course.setScaledContents(True)

        daftar_tanggapan, rating = TanggapanManager.get_course_tanggapan(
            self.course_data)
        for tanggapan in daftar_tanggapan:
            self.show_tanggapan(tanggapan)

        self.window.label_rating_course.setText("⭐ " + str(round(rating, 2)))


        if is_sudah_beli:
            self.window.btn_beli.setText("Tonton Course")
            self.window.btn_berikan_tanggapan.setEnabled(True)
            self.window.btn_beli.clicked.connect(
                self.tonton_course
            )
        else:
            self.window.btn_beli.setText("Beli Course")
            self.window.btn_beli.clicked.connect(
                lambda _: DisplayManager.ins().show("beli_course",
                    course_id=course_id
                )
            )
            self.window.btn_berikan_tanggapan.setEnabled(False)

        # Callback
        self.window.btn_berikan_tanggapan.clicked.connect(
            lambda _: DisplayManager.ins().show("beri_tanggapan", course_id=course_id)
        )
        self.window.btn_back.clicked.connect(
            lambda _: DisplayManager.ins().show("list_course")
        )

    def tonton_course(self):
        '''
        Give course link video to customer
        '''
        subprocess.check_call(
            "echo "+self.course_data.link_video.strip()+"|clip",
            shell=True)
        DisplayManager.ins()\
            .show_success("Menonton Course",
                "Link course: " +
                self.course_data.link_video +
                "\nLink telah dicopy ke clipboard")

    def show_tanggapan(self, tanggapan):
        '''
        Menampilkan tanggapan di view
        '''
        self.i = self.i + 1

        setattr(self, f"tanggapan_{self.i}",
                QtWidgets.QGroupBox(self.window.scrollAreaWidgetContents))
        getattr(self, f"tanggapan_{self.i}").\
            setGeometry(QtCore.QRect(60, 80, 737, 93))
        getattr(self, f"tanggapan_{self.i}").\
            setMinimumSize(QtCore.QSize(0, 93))
        getattr(self, f"tanggapan_{self.i}").\
            setStyleSheet("QGroupBox {\n"
                          "    border : 1px solid black;\n"
                          "}")
        getattr(self, f"tanggapan_{self.i}").\
            setObjectName(f"tanggapan_{self.i}")

        setattr(self, f"hL_{self.i}",
                QtWidgets.QHBoxLayout(getattr(self, f"tanggapan_{self.i}")))
        getattr(self, f"hL_{self.i}").\
            setObjectName(f"hL_{self.i}")
        setattr(self.window, f"tanggapan_{self.i}",
                getattr(self, f"tanggapan_{self.i}"))

        setattr(self, f"frame_{self.i}",
                QtWidgets.QFrame(getattr(self.window, f"tanggapan_{self.i}")))
        getattr(self, f"frame_{self.i}").\
            setObjectName(f"frame_{self.i}")

        setattr(self, f"vL_{self.i}",
                QtWidgets.QVBoxLayout(getattr(self, f"frame_{self.i}")))
        getattr(self, f"vL_{self.i}").\
            setObjectName(f"vL_{self.i}")

        setattr(self, f"label_nama_penanggap_{self.i}",
                QtWidgets.QLabel(getattr(self, f"frame_{self.i}")))
        getattr(self, f"label_nama_penanggap_{self.i}").\
            setMinimumSize(QtCore.QSize(0, 21))
        getattr(self, f"label_nama_penanggap_{self.i}").\
            setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        getattr(self, f"label_nama_penanggap_{self.i}").\
            setFont(font)
        getattr(self, f"label_nama_penanggap_{self.i}").\
            setWordWrap(True)
        getattr(self, f"label_nama_penanggap_{self.i}").\
            setObjectName(f"label_nama_penanggap_{self.i}")
        getattr(self, f"vL_{self.i}").\
            addWidget(getattr(self, f"label_nama_penanggap_{self.i}"))

        setattr(self, f"label_isi_tanggapan_{self.i}",
                QtWidgets.QLabel(getattr(self, f"frame_{self.i}")))
        getattr(self, f"label_isi_tanggapan_{self.i}").\
            setWordWrap(True)
        getattr(self, f"label_isi_tanggapan_{self.i}").\
            setObjectName(f"label_isi_tanggapan_{self.i}")

        getattr(self, f"vL_{self.i}").\
            addWidget(getattr(self, f"label_isi_tanggapan_{self.i}"))
        getattr(self, f"hL_{self.i}").\
            addWidget(getattr(self, f"frame_{self.i}"))

        setattr(self, f"label_rating_penaggap_{self.i}",
                QtWidgets.QLabel(getattr(self, f"tanggapan_{self.i}")))

        getattr(self, f"label_rating_penaggap_{self.i}").\
            setMinimumSize(QtCore.QSize(76, 0))
        getattr(self, f"label_rating_penaggap_{self.i}").\
            setMaximumSize(QtCore.QSize(76, 26))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        getattr(self, f"label_rating_penaggap_{self.i}").\
            setFont(font)
        getattr(self, f"label_rating_penaggap_{self.i}").\
            setObjectName(f"label_rating_penaggap_{self.i}")
        getattr(self, f"hL_{self.i}").\
            addWidget(getattr(self, f"label_rating_penaggap_{self.i}"))

        _translate = QtCore.QCoreApplication.translate
        getattr(self, f"label_nama_penanggap_{self.i}").\
            setText(_translate("Form", tanggapan.pengguna.nama))
        getattr(self, f"label_isi_tanggapan_{self.i}").\
            setText(_translate("Form", tanggapan.review.isi_review))
        getattr(self, f"label_rating_penaggap_{self.i}").\
            setText(_translate("Form", "⭐ " + str(tanggapan.nilai_rating)))

        self.window.verticalLayout_6.\
            addWidget(getattr(self, f"tanggapan_{self.i}"))
