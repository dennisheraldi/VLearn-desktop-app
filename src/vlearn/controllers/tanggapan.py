"""Module for tanggapan manager"""

from typing import List

from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna
from vlearn.models.review import Review
from vlearn.models.tanggapan import Tanggapan


class TanggapanManager:
    """Class for static tanggapan manager.
    """
    @staticmethod
    def get_courses_tanggapan(courses:List[Course]):
        """Get many courses tanggapan.

        Args:
            courses (List[Course]): Courses to look for tanggapan.

        Returns:
            List[Course]: Courses with tanggapan.
        """
        for i in courses:
            i.tanggapan, i.avg_rating = TanggapanManager.get_course_tanggapan(i)
        return courses

    @staticmethod
    def get_course_tanggapan(course:Course):
        """Get all reviews by course.

        Args:
            course (Course): Course reference.

        Returns:
            (list, real): List of review objects and average rating.
        """
        tanggapan:list[Tanggapan] = Tanggapan.all(id_course=course.id_course)
        avg_rating = 0.0
        for i in tanggapan:
            i.pengguna = Pengguna.get(id_pengguna=i.id_pengguna)
            i.review = Review.get(id_review=i.id_review)
            avg_rating += i.nilai_rating
        if len(tanggapan) > 0:
            avg_rating /= len(tanggapan)
        return tanggapan, avg_rating

    @staticmethod
    def add_course_tanggapan(course:Course, pengguna:Pengguna, nilai_rating:float, review:str):
        """Add course tanggapan relationship.

        Args:
            course (Course): Course reference.
            pengguna (Pengguna): Pengguna reference.
            nilai_rating (float): Rating value.
            review (str): Review text.

        Returns:
            Tanggapan: Tanggapan result object create.
        """
        rev = Review.create(
            isi_review=review,
        )
        t = Tanggapan.create(
            id_review=rev.id_review,
            id_course=course.id_course,
            id_pengguna=pengguna.id_pengguna,
            nilai_rating=nilai_rating,
        )
        t.review = rev
        return t
