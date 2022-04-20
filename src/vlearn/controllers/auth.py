"""Module for auth controller.
"""
from vlearn.database import Database
from vlearn.models.pengguna import Pengguna


class AuthController:
    """Class for static auth controller."""
    __LOGGED_USER:Pengguna = None

    @staticmethod
    def get_user():
        """Get current logged in user.

        Returns:
            Pengguna: current user.
        """
        return AuthController.__LOGGED_USER

    @staticmethod
    def login(email, password):
        """Login user to system.

        Args:
            email (str): Email user.
            password (str): Password user.

        Returns:
            bool: Is user successfully login to system.
        """
        p = Pengguna.get(email=email)
        if p is not None and Database.password.verify(p.password, password):
            AuthController.__LOGGED_USER = p
            return True
        return False

    @staticmethod
    def register(nama, email, password, is_admin):
        """Register user to the system.

        Args:
            nama (str): User name.
            email (str): User email.
            password (str): User password.
            isAdmin (bool): Is user admin or not.

        Returns:
            bool: Is user successfully registered to system.
        """
        p = Pengguna.get(email=email)
        if p is None:
            p = Pengguna.create(
                nama=nama,
                email=email,
                password=Database.password.hash(password),
                role='admin' if is_admin else 'user',
            )
            AuthController.__LOGGED_USER = p
            return True
        return False

    @staticmethod
    def logout():
        """Log out current user.
        """
        AuthController.__LOGGED_USER = None

    @staticmethod
    def is_logged_in():
        """Check if there's current user logged in.

        Returns:
            bool: Is there's current user logged in.
        """
        return AuthController.__LOGGED_USER is not None

    @staticmethod
    def is_user_admin():
        """Check if current user (if any) is admin."""
        return AuthController.is_logged_in() and AuthController.__LOGGED_USER.role == 'admin'
