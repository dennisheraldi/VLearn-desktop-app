"""Module for pembelian course controller
"""
from vlearn.controllers.course import CourseManager
from vlearn.controllers.saldo import SaldoManager
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna


class PembelianCourseController:
    """Controller class for PembelianCourse
    """

    @staticmethod
    def beli_course(p: Pengguna, course: Course) -> bool:
        """Method for Pengguna p to buy Course course.

        Args:
            p (Pengguna): Pengguna that will buy course
            course (Course): Course that will be bought

        Returns:
            bool: flag whether the transaction is successful
        """
        if not PembelianCourseController._check_sufficient_balance(p, course):
            return False

        SaldoManager.sub_pengguna_saldo(p, course.harga)

        return not CourseManager.add_course_pengguna(course, p) is None

    @staticmethod
    def _check_sufficient_balance(
            p: Pengguna, course: Course) -> bool:
        """Private method to check whether the balance is sufficient to buy a course.

        Args:
            p (Pengguna): Pengguna that will be checked the balance
            course (Course): Course that will be checked

        Returns:
            bool: flag whether the balance is sufficient
        """
        return SaldoManager.get_pengguna_saldo(p) >= course.harga
