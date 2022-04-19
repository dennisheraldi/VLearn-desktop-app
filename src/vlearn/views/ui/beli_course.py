# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beli_course.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.widget.setStyleSheet("background-color: #180156;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_5)
        self.widget_2.setMaximumSize(QtCore.QSize(600, 400))
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setStyleSheet("background-color: #fff;\n"
"border-radius: 16px;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(10, 20, 560, 275))
        self.widget_4.setStyleSheet("QWidget{\n"
"border: 3px solid #777;\n"
"border-radius: 12px;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 521, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(40, 210, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#b5ffd9;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#a5f0cc;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#a0d6b9;\\n\"\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 210, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:#b5ffd9;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#a5f0cc;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#a0d6b9;\\n\"\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "Menu Pembelian"))
        self.label_2.setText(_translate("MainWindow", "placeholder1"))
        self.label_3.setText(_translate("MainWindow", "placeholder2"))
        self.pushButton.setText(_translate("MainWindow", "Batal"))
        self.pushButton_2.setText(_translate("MainWindow", "Lanjut"))
