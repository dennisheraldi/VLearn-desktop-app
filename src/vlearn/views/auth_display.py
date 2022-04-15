from vlearn.controllers.auth import *
from vlearn.views.display import AppDisplay, DisplayManager


class ViewAuth(object):
    class Login(AppDisplay):
        '''
        View untuk login
        '''
        def __init__(self):
            '''
            Buat view menu utama login
            '''
            # UI setup
            from vlearn.views.ui.login import Ui_MainWindow
            super().__init__(Ui_MainWindow)

            email = self.window.input_email.text()
            password = self.window.input_email.text()

            # Callback
            self.window.link_register.mousePressEvent = lambda _: DisplayManager.ins().show('auth.register')
            self.window.btn_login.clicked.connect(lambda _: self.login(email, password))
            
        def login(self, email, password):
            success = AuthController.login(email, password)
            if not success:
                DisplayManager.ins().show_error("Login Failed", "Username or password incorrect")


    class Register(AppDisplay):
        '''
        View untuk register
        '''
        def __init__(self):
            from vlearn.views.ui.register import Ui_MainWindow
            super().__init__(Ui_MainWindow)

            name = self.window.input_name.text()
            email = self.window.input_email.text()
            password = self.window.input_password.text()

            # Callback
            self.window.link_login.mousePressEvent = lambda _: DisplayManager.ins().show('auth.login')
            self.window.btn_register.clicked.connect(lambda _: self.register(name, email, password))

        def register(self, name, email, password):
            success = AuthController.register(name, email, password, False)
            if not success:
                DisplayManager.ins().show_error("Register Failed", "Invalid input")
            else:
                DisplayManager.ins().show_success("Register Success", "Register success")
                DisplayManager.ins().show('auth.login')

