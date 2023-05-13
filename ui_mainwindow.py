# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qlnpte import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(19, 86, 120);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(200, 35))
        self.btn_menu.setMaximumSize(QSize(16777215, 35))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	alternate-background-color: rgb(60, 115, 120);\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(60, 100, 120);\n"
"	font: 87 12pt \"Arial Black\";\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/9135949.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(656, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMaximumSize(QSize(16777215, 35))
        self.btn_minimizar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:10px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/786263.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.frame_superior)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setMaximumSize(QSize(16777215, 35))
        self.btn_restaurar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:5px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/159100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMaximumSize(QSize(16777215, 35))
        self.btn_maximizar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:5px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/204538.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMaximumSize(QSize(16777215, 35))
        self.btn_cerrar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:10px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/1828774.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(200, 0))
        self.frame_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 85, 120);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(50, 84, 100);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_editor = QPushButton(self.frame_menu)
        self.btn_editor.setObjectName(u"btn_editor")
        self.btn_editor.setMinimumSize(QSize(0, 40))
        self.btn_editor.setMaximumSize(QSize(16777215, 40))
        self.btn_editor.setLayoutDirection(Qt.LeftToRight)
        self.btn_editor.setAutoFillBackground(False)
        self.btn_editor.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_editor.setText(u"         Editor")
        icon5 = QIcon()
        icon5.addFile(u"images/1994335.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editor.setIcon(icon5)
        self.btn_editor.setIconSize(QSize(40, 40))
        self.btn_editor.setCheckable(False)
        self.btn_editor.setChecked(False)
        self.btn_editor.setAutoExclusive(False)
        self.btn_editor.setAutoDefault(False)
        self.btn_editor.setFlat(False)

        self.verticalLayout_3.addWidget(self.btn_editor)

        self.btn_errores = QPushButton(self.frame_menu)
        self.btn_errores.setObjectName(u"btn_errores")
        self.btn_errores.setMinimumSize(QSize(0, 40))
        self.btn_errores.setMaximumSize(QSize(16777215, 40))
        self.btn_errores.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"images/921564.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_errores.setIcon(icon6)
        self.btn_errores.setIconSize(QSize(35, 35))
        self.btn_errores.setCheckable(False)
        self.btn_errores.setChecked(False)
        self.btn_errores.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_errores)

        self.btn_analizar = QPushButton(self.frame_menu)
        self.btn_analizar.setObjectName(u"btn_analizar")
        self.btn_analizar.setMinimumSize(QSize(0, 40))
        self.btn_analizar.setMaximumSize(QSize(16777215, 40))
        self.btn_analizar.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"images/3159355.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analizar.setIcon(icon7)
        self.btn_analizar.setIconSize(QSize(43, 43))
        self.btn_analizar.setCheckable(False)
        self.btn_analizar.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_analizar)

        self.btn_correr = QPushButton(self.frame_menu)
        self.btn_correr.setObjectName(u"btn_correr")
        self.btn_correr.setMinimumSize(QSize(0, 40))
        self.btn_correr.setMaximumSize(QSize(16777215, 40))
        self.btn_correr.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u"images/5486216.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_correr.setIcon(icon8)
        self.btn_correr.setIconSize(QSize(60, 60))
        self.btn_correr.setCheckable(False)
        self.btn_correr.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_correr)

        self.verticalSpacer = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_menu)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = PlainTextEdit(self.frame_contenedor)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font: 9pt \"Courier New\";")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_editor.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"   MENU", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_errores.setText(QCoreApplication.translate("MainWindow", u"        Errores", None))
        self.btn_analizar.setText(QCoreApplication.translate("MainWindow", u"        Analizar", None))
        self.btn_correr.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Universidad de Guadalajara", None))
    # retranslateUi

