"""Module for beli course page controller
"""
import locale

from vlearn.controllers.auth import AuthController
from vlearn.controllers.pembelian_course import PembelianCourseController
from vlearn.models.course import Course
from vlearn.views.display import AppDisplay, DisplayManager
from vlearn.views.ui.beli_course import Ui_MainWindow


class BeliCourseDisplay(AppDisplay):
    '''
    View untuk display pembelian course
    '''

    def __init__(self, course_id):
        super().__init__(Ui_MainWindow)

        self.course_id = course_id

        course = Course.get(id_course=self.course_id)
        user = AuthController.get_user()

        locale.setlocale(locale.LC_ALL, '')

        self.window.label_2.setText(
            f'Apakah anda ingin membeli course {course.judul}\
dengan harga {locale.currency(course.harga, grouping=True)}?'
        )

        self.window.label_3.setText(
            f'Saldo anda: {locale.currency(user.saldo, grouping=True)}'
        )

        self.window.pushButton.clicked.connect(self.batal)
        self.window.pushButton_2.clicked.connect(self.lanjut)

    def batal(self):
        """Method to cancel beli course operation
        """

        DisplayManager.ins().show('detail_course', course_id=self.course_id)

    def lanjut(self):
        """Method to do beli course operation
        """

        course = Course.get(id_course=self.course_id)
        user = AuthController.get_user()

        if PembelianCourseController.beli_course(user, course):
            DisplayManager.ins().show_success('Pembelian sukses',
                                              'Anda telah sukses membeli course ini')
            DisplayManager.ins().show('detail_course', course_id=self.course_id)
        else:
            DisplayManager.ins().show_error('Pembelian gagal', 'Saldo anda tidak cukup')
