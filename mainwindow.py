from ui_mainwindow import *
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Lista  de instrucciones reconocidas
        self.tabop = ("AAA", "AAD", "AAM", "AAS", "ADC", "ADD", "AND", "CALL", "CBW", "CLC",
         "CLD", "CLI", "CMC", "CMP", "CMPSB", "CMPSW", "CWD", "DAA", "DAS",
         "DEC", "DIV", "HLT", "IDIV", "IMUL", "IN", "INC", "INT", "INTO", "IRET",
         "JA", "JAE", "JB", "JBE", "JC", "JCXZ", "JE", "JG", "JGE", "JL", "JLE", "JMP",
         "JNA", "JNAE", "JNB", "JNBE", "JNC", "JNE", "JNG", "JNGE", "JNL", "JNLE",
         "JNO", "JNP", "JNS", "JNZ", "JO", "JP", "JPE", "JPO", "JS", "JZ", "LAHF",
         "LDS", "LEA", "LES", "LODSB", "LODSW", "LOOP", "LOOPE", "LOOPNE", "LOOPNZ",
         "LOOPZ", "MOV", "MOVSB", "MOVSW", "MUL", "NEG", "NOP", "NOT", "OR", "OUT",
         "POP", "POPA", "POPF", "PUSH", "PUSHF", "RCL", "RCR", "REP", "REPE", "REPNE",
         "REPNZ", "REPZ", "RET", "RETF", "ROL", "ROR", "SAHF", "SAL", "SAR", "SBB", "SCASB",
         "SCASW", "SHL", "SHR", "STC", "STD", "STI" "TOSB", "STOSW", "SUB", "TEST", "XCHG",
         "XLATB", "XOR", ".ORG", "ORG", "PROC", "ENDP", "END", "NAME", "INCLUDE")
        
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
        self.ui.btn_editor.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.pg_editor)])
        self.ui.btn_errores.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.pg_errores)])
        self.ui.btn_analizar.clicked.connect(lambda: [self.ui.stackedWidget.setCurrentWidget(self.ui.pg_analisis)])
        
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
    def salir(self):                                    # Funcion para cerrar ventana
        self.close()                    
    def minimizar(self):                                # Funcion para minimizar ventana
        self.showMinimized()
    def normal(self):                                   # Funcion para restaurar ventana
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()
    def maximizar(self):                                # Funcion para maximizar ventana
        self.showMaximized()
        self.ui.btn_restaurar.show()
        self.ui.btn_maximizar.hide()
    def mostrar_menu(self):                             # Funcion para invertir mostrar/ocultar menu
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
    def resizeEvent(self, event):                       # Funcion para modificar el tamaño de la ventana
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    # Mover ventana
    def mousePressEvent(self, event):                   # Detectar click del mouse
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):                     # Funcion para mover la ventana
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()
            
    def error(self):                                    # Funcion para resaltar lineas de codigo en rojo
        self.ui.plainTextEdit_codigo.highlight_error_lines(self.procesar_codigo(self.read_lines()))
        
    def read_lines(self):                               # Lee todas las lineas del plaintext de codigo
        contenido = self.ui.plainTextEdit_codigo.toPlainText()
        lista_lineas = contenido.split('\n')
        return lista_lineas                             # Regresa una lista de lineas
    
    def procesar_codigo(self, lista_lineas):            # Procesador de texto (descompone cada linea en componentes como: Instruccion, operadores, comentarios)
        instruccion = ""
        instruccion_operando = ""
        operandos = [""]
        lista_erroes = []
        linea_comentario = [""]
        contador_linea = 0
        for linea in lista_lineas:
            contador_linea += 1
            if linea:
                try:
                    linea_vacia = linea.strip()
                    componentes = linea.split(';')                # Separar la línea por '; '
                    instruccion_ope = componentes[0].split()      # Separar la primera parte de componentes por espacios
                    instruccion = instruccion_ope[0]              # Obtener la instruccion de la linea
                    try:
                        operandos = instruccion_ope[1:] if len(instruccion_ope) > 1 else []
                        operandos = operandos[0].split(",")       # Obtener los operandos de la instruccion
                        comentario = componentes[1].strip() if len(componentes) > 1 else ""
                    except:
                        operandos = [""]
                        comentario = ""
                except:
                    instruccion = ""
                try:
                    instruccion_operando = operandos[0].upper()
                except:
                    pass
            if instruccion.upper() in self.tabop: # INSTRUCCION VALIDA (VERIFICAR OPERADORES)
                if linea != "":
                    print('La linea "{}" es una linea valida!'.format(linea))
                    print('La instruccion es: "{}", el o los operadores son: "{}", y el comentario es: "{}"'.format(instruccion, operandos, comentario))
            elif instruccion_operando in self.tabop:   # La instruccion no está en el primer espacio de instruccion[0]
                try:
                    # VALIDAR QUE HAY UNA ETIQUETA ANTES DE LA INSTRUCCION !!!!!
                    # VALIDAR LAS SUBRUTINAS (BANDERA QUE ABRE EN PROC Y OTRA QUE CIERRA EN ENDP) (MARCAR TODAS LAS LINEAS INTERMEDIAS EN ROJO)
                    # VALIDAR DATA SEGMENT
                    # CREAR AUTOMATAS PARA VALIDAR OPERADORES Y TIPOS DE DATOS
                    # MODIFICAR LAS EXCEPCIONES (HACER ESPECIFICAS) PARA EVITAR OCULTAR OTROS FALLOS
                    # AGREGAR FUNCIONALIDAD A LAS DEMAS PAGINAS O ELIMINARLAS (ERROES | ANALIZAR)
                    if instruccion_ope[1].upper() in self.tabop: # INSTRUCCION VALIDA (VERIFICAR OPERADORES)
                        instruccion = instruccion_ope[1]
                        operandos = instruccion_ope[2:] if len(instruccion_ope) > 1 else []
                        operandos = operandos[0].split(",")
                        comentario = componentes[1].strip() if len(componentes) > 1 else ""
                        print('La linea "{}" es una linea valida!'.format(linea))
                        print('La instruccion es: "{}", el o los operadores son: "{}", y el comentario es: "{}"'.format(instruccion, operandos, comentario))
                except:
                    pass
            elif (linea and linea_vacia != "") and (':' not in instruccion) and ("DEFINE" not in instruccion.upper()):
                linea_comentario = linea_vacia.split()  # No se encontró una instruccion valida.
                if ";" not in linea_comentario[0]:  # No se encontró ni un comentario, ni una linea en blanco ni una definicion ni una etiqueta.
                    print(linea, " Sin instruccion")        # INSTRUCCION INVALIDA (RECHAZADA)
                    lista_erroes.append(contador_linea)     # Se agrega la linea actual a la lista de errores
        return lista_erroes        
        
    
    