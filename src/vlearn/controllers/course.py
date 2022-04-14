"""Module for course controller
"""
from typing import List

from vlearn.models.base import Model
from vlearn.models.course import Course
from vlearn.models.pengguna import Pengguna


class CoursePengguna(Model):
    """Class for course pengguna relationship model.
    """
    TABLE = 'course_pengguna'
    CREATE_QUERY = """
        CREATE TABLE IF NOT EXISTS `course_pengguna` (
            `id_course` INTEGER NOT NULL,
            `id_pengguna` INTEGER NOT NULL,
            `waktu_pembelian` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id_course`, `id_pengguna`),
            FOREIGN KEY (`id_course`) REFERENCES courses(`id_course`) ON DELETE CASCADE,
            FOREIGN KEY (`id_pengguna`) REFERENCES pengguna(`id_pengguna`) ON DELETE CASCADE
        );
    """
    PRIMARY_KEY = ['id_course', 'id_pengguna']
    ATTRIBUTES = ['id_course', 'id_pengguna', 'waktu_pembelian']

    def __init__(self, id_course: int, id_pengguna: int, waktu_pembelian=None):
        self.id_course = id_course
        self.id_pengguna = id_pengguna
        self.waktu_pembelian = waktu_pembelian
        super().__init__()

class CourseManager:
    """Class for static course manager.
    """
    @staticmethod
    def get_courses_pengguna(pengguna:Pengguna) -> List[Course]:
        """Get all courses by pengguna.

        Args:
            pengguna (Pengguna): Pengguna reference.

        Returns:
            list: List of course objects owned by pengguna.
        """
        course_pengguna:List[CoursePengguna] = CoursePengguna.all(
            id_pengguna=pengguna.id_pengguna
        )
        # Prevent overhead for resizing dynamic array
        courses:List[Course] = [None for _ in range(len(course_pengguna))]
        for i, v in enumerate(course_pengguna):
            courses[i] = Course.get(id_course=v.id_course)
        return courses

    @staticmethod
    def add_course_pengguna(course:Course, pengguna:Pengguna):
        """Add course pengguna relationship.

        Args:
            course (Course): Course reference.
            pengguna (Pengguna): Pengguna reference.

        Returns:
            CoursePengguna: CoursePengguna reference.
        """
        return CoursePengguna.create(
            id_course=course.id_course,
            id_pengguna=pengguna.id_pengguna
        )
