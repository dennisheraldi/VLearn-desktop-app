"""Module for list course page controller
"""

from vlearn.controllers.auth import AuthController
from vlearn.controllers.course import CourseManager
from vlearn.controllers.tanggapan import TanggapanManager
from vlearn.models.course import Course
from vlearn.views.display import AppDisplay
from vlearn.views.ui.list_course import Ui_MainWindow


class ListCourseDisplay(AppDisplay):
    """
    View untuk display semua course
    """

    def __init__(self):
        super().__init__(Ui_MainWindow)

        self.window.injectData(get_data(is_all=True))
        self.window.injectFecthFunc(get_data)
        self.window.setPage(0)


def get_data(is_all):
    """Fetch function to get courses data

    Args:
        is_all (bool): flag whether to get all courses or user's courses only

    Returns:
        list[Course]: courses data
    """

    user = AuthController.get_user()
    courses = Course.all() if is_all else CourseManager.get_courses_pengguna(user)

    return TanggapanManager.get_courses_tanggapan(courses)
