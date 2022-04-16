'''Module implementation of authorization display view.
'''

from vlearn.controllers.auth import AuthController
from vlearn.views.display import AppDisplay, DisplayManager
from vlearn.views.ui.login import Ui_MainWindow as Ui_Login
from vlearn.views.ui.register import Ui_MainWindow as Ui_Register


class ViewAuth():
    '''
    View untuk login dan register
    '''
    class Login(AppDisplay):
        '''
        View untuk login
        '''
        def __init__(self):
            '''
            Buat view menu utama login
            '''
            # UI setup
            super().__init__(Ui_Login)

            email = self.window.input_email.text()
            password = self.window.input_password.text()

            # Callback
            self.window.link_register.mousePressEvent = \
                lambda _: DisplayManager.ins().show('auth.register')
            self.window.btn_login.clicked.connect(
                lambda _: login(email, password))
    class Register(AppDisplay):
        '''
        View untuk register
        '''
        def __init__(self):
            super().__init__(Ui_Register)

            name = self.window.input_name.text()
            email = self.window.input_email.text()
            password = self.window.input_password.text()

            # Callback
            self.window.link_login.mousePressEvent = \
                lambda _: DisplayManager.ins().show('auth.login')
            self.window.btn_register.clicked.connect(
                lambda _: register(name, email, password))


def login(email, password):
    '''
    Menangani login pengguna
    '''
    success = AuthController.login(email, password)
    if not success:
        DisplayManager.ins().show_error('Login Failed',
            'Username or password incorrect')

def register(name, email, password):
    '''
    Menagani regristasi pengguna baru
    '''
    success = AuthController.register(name, email, password, False)
    if not success:
        DisplayManager.ins()\
            .show_error('Register Failed', 'Invalid input')
    else:
        DisplayManager.ins()\
            .show_success('Register Success', 'Register success')
        DisplayManager.ins()\
            .show('auth.login')
