'''Module implementation of beri tanggapan display view.
'''

from vlearn.controllers.auth import AuthController
from vlearn.controllers.tanggapan import TanggapanManager
from vlearn.models.course import Course
from vlearn.views.display import AppDisplay, DisplayManager
from vlearn.views.ui.beri_tanggapan import Ui_MainWindow as Ui_Beri_Tanggapan


class ViewBeriTanggapan(AppDisplay):
    '''
    View untuk login
    '''
    def __init__(self, course_id):
        '''
        Buat view menu utama login
        '''
        # UI setup
        super().__init__(Ui_Beri_Tanggapan)

        self.course_id = course_id

        # Callback
        self.window.btn_kirim.clicked.connect(self.add_tanggapan)
        self.window.btn_kembali.clicked.connect(
            lambda _: DisplayManager.ins().show('detail_course', course_id = course_id)
        )



    def add_tanggapan(self):
        '''
        Add tanggapan to database
        '''
        rating = self.window.spinBox.text()
        review = self.window.textEdit.toPlainText()

        rating = float(rating.replace(',', '.'))
        TanggapanManager.add_course_tanggapan(
            Course.get(id_course=self.course_id),
            AuthController.get_user(), rating, review)
        DisplayManager.ins().show_success('Success',
            'Tanggapan added successfully')
        DisplayManager.ins().show('detail_course',
            course_id = self.course_id)
