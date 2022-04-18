# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/list_course.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 575)
        # MainWindow.setWidth(900)
        MainWindow.setStyleSheet("QPushButton:pushButton {\n"
                                 "    background-color:rgb(63, 1, 255);\n"
                                 "    color:\"white\"\n"
                                 "}\n"
                                 "\n"
                                 "QWidget{\n"
                                 "    background-color:rgb(24, 1, 86);\n"
                                 "    border-radius:3%\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea {\n"
                                 "    border-radius:20%;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidgetLayout = QtWidgets.QVBoxLayout()
        self.centralwidget.setLayout(self.centralwidgetLayout)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.centralwidgetLayout.addWidget(
            self.layoutWidget, 0, QtCore.Qt.AlignTop)

        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 861, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(120)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isiSaldoButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.isiSaldoButton.sizePolicy().hasHeightForWidth())
        self.isiSaldoButton.setSizePolicy(sizePolicy)
        self.isiSaldoButton.setMinimumSize(QtCore.QSize(130, 35))
        self.isiSaldoButton.setMaximumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.isiSaldoButton.setFont(font)
        self.isiSaldoButton.setStyleSheet("QPushButton{\n"
                                          "    background-color:#b5ffd9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color:#a5f0cc;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "    background-color:#a0d6b9;\n"
                                          "}")
        self.isiSaldoButton.setObjectName("isiSaldoButton")
        self.horizontalLayout.addWidget(self.isiSaldoButton)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
                                   "    color:\"white\"\n"
                                   "}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.changeDataButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.changeDataButton.sizePolicy().hasHeightForWidth())
        self.changeDataButton.setSizePolicy(sizePolicy)
        self.changeDataButton.setMinimumSize(QtCore.QSize(140, 35))
        self.changeDataButton.setMaximumSize(QtCore.QSize(140, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.changeDataButton.setFont(font)
        self.changeDataButton.setStyleSheet("QPushButton{\n"
                                            "    background-color:#b5ffd9;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color:#a5f0cc;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color:#a0d6b9;\n"
                                            "}")
        self.changeDataButton.setObjectName("changeDataButton")
        self.horizontalLayout.addWidget(self.changeDataButton)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.centralwidgetLayout.addWidget(
            self.widget, 0, QtCore.Qt.AlignBottom)

        self.widget.setGeometry(QtCore.QRect(20, 80, 861, 441))
        self.widget.setStyleSheet("background-color:#ae01fb;\n"
                                  "border-radius:10%;")
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.isAllCourse = True
        self.SIZE = 6

        self.content = QtWidgets.QVBoxLayout()
        self.content.setSpacing(20)
        self.widget.setLayout(self.content)

        self.pageButtons = QtWidgets.QWidget(self.centralwidget)
        self.layoutPageButtons = QtWidgets.QHBoxLayout()
        self.pageButtons.setLayout(self.layoutPageButtons)

        self.isiSaldoButton.clicked.connect(
            lambda: print("OPENING ISI SALDO PAGE"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.isiSaldoButton.setText(_translate("MainWindow", "Isi Saldo"))
        self.label_9.setText(_translate("MainWindow", "Daftar Semua Course"))
        self.changeDataButton.setText(_translate("MainWindow", "Course Saya"))

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def injectData(self, data):
        self.data = data

        self.clearLayout(self.pageButtons.layout())

        btnCount = len(data) // 6 + (1 if len(data) % 6 != 0 else 0)
        for i in range(btnCount):
            pushButton = QtWidgets.QPushButton(self.pageButtons)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                pushButton.sizePolicy().hasHeightForWidth())
            pushButton.setSizePolicy(sizePolicy)
            pushButton.setMinimumSize(QtCore.QSize(25, 25))
            pushButton.setMaximumSize(QtCore.QSize(25, 25))

            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(75)
            pushButton.setFont(font)

            pushButton.setStyleSheet("QPushButton{\n"
                                     "    background-color:#b5ffd9;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:#a5f0cc;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#a0d6b9;\n"
                                     "}")

            pushButton.setText(str(i+1))

            pushButton.clicked.connect(lambda _, x=i: self.setPage(x))

            self.layoutPageButtons.addWidget(
                pushButton, 0, QtCore.Qt.AlignCenter)

        self.centralwidgetLayout.addWidget(self.pageButtons)

    def setPage(self, page):
        slicedData = [self.data[(page*self.SIZE) + i] if ((page*self.SIZE) +
                                                          i < len(self.data)) else None for i in range(self.SIZE)]

        self.clearLayout(self.widget.layout())
        self.injectedWidgets = []
        for i in range(len(slicedData)):
            widget = QtWidgets.QWidget(self.widget)
            if (not slicedData[i] is None):
                widget.setStyleSheet(f"background-color:#fff;\n")
                layout = QtWidgets.QHBoxLayout()
                widget.setLayout(layout)

                pixmap = QtGui.QPixmap('static/imgs/icon.jpg')
                imgLabel = QtWidgets.QLabel(widget)
                imgLabel.setPixmap(pixmap)
                imgLabel.setFixedSize(30, 30)
                layout.addWidget(imgLabel)

                label = QtWidgets.QLabel(widget)
                label.setText(slicedData[i].judul)
                layout.addWidget(label)

                rightWidget = QtWidgets.QWidget(widget)
                rightLayout = QtWidgets.QHBoxLayout()
                rightWidget.setLayout(rightLayout)

                pixmap2 = QtGui.QPixmap('static/imgs/icon.jpg')
                imgLabel2 = QtWidgets.QLabel(rightWidget)
                imgLabel2.setPixmap(pixmap2)
                imgLabel2.setFixedSize(30, 30)
                rightLayout.addWidget(imgLabel2)

                label2 = QtWidgets.QLabel(rightWidget)
                label2.setText(str(round(slicedData[i].avg_rating, 2)))
                rightLayout.addWidget(label2)
                rightLayout.setContentsMargins(0, 0, 0, 0)

                layout.addWidget(rightWidget, 0, QtCore.Qt.AlignRight)

                widget.mouseReleaseEvent = lambda _, x=slicedData[i].id_course: self.openCourse(
                    x)
            else:
                widget.setFixedHeight(50)
            self.content.addWidget(widget)
            self.injectedWidgets.append(widget)

    def injectFecthFunc(self, func):
        self.changeDataButton.clicked.connect(lambda: self.changeData(func))

    def changeData(self, func):
        self.isAllCourse = not self.isAllCourse

        self.label_9.setText(
            "Daftar Semua Course" if self.isAllCourse else "Daftar Course Saya")
        self.changeDataButton.setText(
            "Course Saya" if self.isAllCourse else "Semua Course")

        self.clearLayout(self.pageButtons.layout())
        self.injectData(func(self.isAllCourse))
        self.setPage(0)

    def openCourse(self, idx):
        print(f"OPENING COURSE {idx}")
