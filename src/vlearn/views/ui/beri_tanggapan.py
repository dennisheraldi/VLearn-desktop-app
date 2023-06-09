# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beri_tanggapan.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 586)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:rgb(24, 1, 86)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color:rgb(24, 1, 86)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(451, 301))
        self.groupBox_2.setMaximumSize(QtCore.QSize(451, 301))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"background-color:\"white\";\n"
"border-radius: 5%;\n"
"border: 1px solid black\n"
"\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:white\n"
"}\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 391, 191))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"background-color:\"white\";\n"
"border-radius: 5%;\n"
"border:1px solid black\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 12, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(120, 10, 45, 22))
        self.spinBox.setStyleSheet("QDoubleSpinBox {\n"
"    background-color: #c8c4c4;\n"
"    border-radius:5%;\n"
"}")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 371, 121))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #c8c4c4;\n"
"    border-radius:5%;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_kirim = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_kirim.setGeometry(QtCore.QRect(350, 260, 75, 23))
        self.btn_kirim.setStyleSheet("QPushButton {\n"
"    background-color:#3f01ff;\n"
"    color:#fff;\n"
"    padding: 2px;\n"
"    border-radius: 5%;\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#3000e0;\n"
"    color:#fff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:#2000c0;\n"
"    color:#fff;\n"
"}")
        self.btn_kirim.setObjectName("btn_kirim")
        self.btn_kembali = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_kembali.setGeometry(QtCore.QRect(30, 260, 75, 23))
        self.btn_kembali.setStyleSheet("QPushButton{\n"
"    background-color:#b5ffd9;\n"
"    border : 1px solid black;\n"
"    border-radius: 5%\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#a5f0cc;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:#a0d6b9;\n"
"}")
        self.btn_kembali.setObjectName("btn_kembali")
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "⭐ Rating anda"))
        self.label_2.setText(_translate("MainWindow", "📰 Review anda"))
        self.label_3.setText(_translate("MainWindow", "Tanggapan"))
        self.btn_kirim.setText(_translate("MainWindow", "Kirim"))
        self.btn_kembali.setText(_translate("MainWindow", "Kembali"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
