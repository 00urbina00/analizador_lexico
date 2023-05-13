from ui_mainwindow import *
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Eventos ----------------------------------------------------------------
        
        # Eliminar barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Sizerip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        # Mover ventana
        self.ui.frame_superior.mouseMoveEvent =  self.mover_ventana # Hacer funcion 
        
        # Acceder a las paginas
        # self.ui.btn_inicio.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.pg_inicio)])

        # Control de barra de titulos
        self.ui.btn_minimizar.clicked.connect(self.minimizar)
        self.ui.btn_restaurar.clicked.connect(self.normal)
        self.ui.btn_maximizar.clicked.connect(self.maximizar)
        self.ui.btn_cerrar.clicked.connect(self.salir)
        self.ui.btn_restaurar.hide()
        
        # Menu lateral
        self.ui.btn_menu.clicked.connect(self.mostrar_menu)

        # Botones
        # -------------------------------------------------------------------------------
        self.ui.btn_correr.clicked.connect(self.error)
        
        # Ajustar Tablas
        # self.ui.tabla_viajes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        
    # Funciones interfaz
    # -----------------------------------------------------------------------------------
    def salir(self):
        self.close()
    def minimizar(self):
        self.showMinimized()
    def normal(self):
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()
    def maximizar(self):
        self.showMaximized()
        self.ui.btn_restaurar.show()
        self.ui.btn_maximizar.hide()
    def mostrar_menu(self):
        if True:
            width = self.ui.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    # SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    # Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()
            
    def error(self):
        n = [1, 3, 4, 7]
        self.ui.plainTextEdit.highlight_error_lines(n)