from ui_mainwindow import *
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation

from automata_er import Automata

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.animacion = None
        self.clickPosition = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.automata_ds = Automata(estados_ds, estado_inicial_ds, estados_aceptacion_ds, transiciones_ds)
        self.dict_tabop = {"AAA": 0, "AAD": 0, "AAM": 0, "AAS": 0, "ADC": 2, "ADD": 2, "AND": 2, "CALL": 1, "CBW": 0,
                           "CLC": 0, "CLD": 0, "CLI": 0, "CMC": 0, "CMP": 2, "CMPSB": 0, "CMPSW": 0, "CWD": 0, "DAA": 0,
                           "DAS": 0, "DEC": 1, "DIV": 1, "HLT": 0, "IDIV": 1, "IMUL": 1, "IN": 2, "INC": 1, "INT": 1,
                           "INTO": 0, "IRET": 0, "JA": 1, "JAE": 1, "JB": 1, "JBE": 1, "JC": 1, "JCXZ": 1, "JE": 1,
                           "JG": 1, "JGE": 1, "JL": 1, "JLE": 1, "JMP": 1, "JNA": 1, "JNAE": 1, "JNB": 1, "JNBE": 1,
                           "JNC": 1, "JNE": 1, "JNG": 1, "JNGE": 1, "JNL": 1, "JNLE": 1, "JNO": 1, "JNP": 1, "JNS": 1,
                           "JNZ": 1, "JO": 1, "JP": 1, "JPE": 1, "JPO": 1, "JS": 1, "JZ": 1, "LAHF": 0, "LDS": 2,
                           "LEA": 2, "LES": 2, "LODSB": 0, "LODSW": 0, "LOOP": 1, "LOOPE": 1, "LOOPNE": 1, "LOOPNZ": 1,
                           "LOOPZ": 1, "MOV": 2, "MOVSB": 0, "MOVSW": 0, "MUL": 2, "NEG": 2, "NOP": 0, "NOT": 2,
                           "OR": 2, "OUT": 2, "POP": 2, "POPA": 0, "POPF": 0, "PUSH": 2, "PUSHF": 0, "RCL": 2, "RCR": 2,
                           "REP": 0, "REPE": 0, "REPNE": 0, "REPNZ": 0, "REPZ": 0, "RET": 0, "RETF": 0, "ROL": 0,
                           "ROR": 0, "SAHF": 0, "SAL": 0, "SAR": 0, "SBB": 0, "SCASB": 0, "SCASW": 0, "SHL": 0,
                           "SHR": 0, "STC": 0, "STD": 0, 'STI': 0, 'TOSB': 0, 'STOSW': 0, 'SUB': 2, 'TEST': 2,
                           'XCHG': 2, 'XLATB': 0, 'XOR': 2, 'END': 0, 'NAME': 0, 'INCLUDE': 0, 'ORG': 0, '.ORG': 0,
                           'PROC': 0, 'ENDP': 0}

        # Lista de instrucciones reconocidas
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
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana  # Hacer funcion

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
    def salir(self):  # Funcion para cerrar ventana
        self.close()

    def minimizar(self):  # Funcion para minimizar ventana
        self.showMinimized()

    def normal(self):  # Funcion para restaurar ventana
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()

    def maximizar(self):  # Funcion para maximizar ventana
        self.showMaximized()
        self.ui.btn_restaurar.show()
        self.ui.btn_maximizar.hide()

    def mostrar_menu(self):  # Funcion para invertir mostrar/ocultar menu
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
    def resizeEvent(self, event):  # Funcion para modificar el tamaño de la ventana
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana
    def mousePressEvent(self, event):  # Detectar click del mouse
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):  # Funcion para mover la ventana
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

    def error(self):  # Funcion para resaltar lineas de codigo en rojo
        self.ui.plainTextEdit_codigo.highlight_error_lines(self.procesar_codigo(self.read_lines()))

    def read_lines(self):  # Lee todas las líneas del plaintext de codigo
        contenido = self.ui.plainTextEdit_codigo.toPlainText()
        lista_lineas = contenido.split('\n')
        return lista_lineas  # Regresa una lista de lineas

    # Procesador de texto (descompone cada linea en componentes como: Instruccion, operadores, comentarios)
    def procesar_codigo(self, lista_lineas):
        contador_linea = 0
        lista_erroes = []  # Guarda el numero de lineas donde se detectó un error
        pila_llamadas_procedimientos = ['#']  # Guarda cada inicio de una subrutina (# es pila vacía)
        for linea in lista_lineas:
            linea_vacia = ""
            contador_linea += 1  # Cuenta cuantas lineas se han leído
            sub_rutina = ""  # Nombre de la subrutina si es que hay
            instruccion_ope = [""]  # Separa todos los componentes de la linea sin tomar comentarios
            instruccion = ""  # Cuando la instruccion se encuentra en el primer indice [0]
            instruccion_operando = ""  # Cuando la instruccion se encuentra en el segundo indice [1]
            operandos = [""]  # Arroja los operandos de una instrucción ("ax, bx" en "mov ax, bx")
            componentes = [""]
            linea_comentario = [""]  # Guarda una linea completa si solo contiene un comentario
            linea_proc = 0

            if linea:
                linea_vacia = linea.strip()
                componentes = linea.split(';')  # Separar la línea por '; '
                instruccion_ope = componentes[0].split()  # Separar la primera parte de componentes por espacios
                try:
                    instruccion = instruccion_ope[0]  # Obtener la instruccion de la linea
                except IndexError:
                    pass  # DEBUG!!!
                    # print('instruccion_ope no contiene elementos en la posicion [0]')
                operandos = instruccion_ope[1:] if len(instruccion_ope) > 1 else []
                try:
                    operandos = operandos[0].split(",")  # Obtener los operandos de la instruccion
                except IndexError:
                    pass  # DEBUG!!!
                    # print("Operandos no contiene elementos en la posicion [0]")
                comentario = componentes[1].strip() if len(componentes) > 1 else ""
                try:
                    instruccion_operando = operandos[0].upper()
                except IndexError:
                    pass
                    # print("error")
            ############################################################################################################
            # INICIA VALIDACION
            ############################################################################################################
            if instruccion.upper() in self.dict_tabop:  # INSTRUCCION VALIDA (VERIFICAR OPERADORES)
                # Se encontró una instruccion valida
                if linea != "":
                    pass
                    # print('La linea "{}" es una linea valida!'.format(linea))
                    # print('La instruccion es: "{}", el o los operadores son: "{}", y el comentario es: "{}"'.
                    # format(instruccion, operandos, comentario))
            elif instruccion_operando in self.dict_tabop:
                # Se encontró una instruccion válida en el segundo espacio (después de otro elemento)
                if instruccion_ope[1].upper() in self.dict_tabop:  # INSTRUCCION VALIDA (VERIFICAR OPERADORES)
                    if ":" in instruccion_ope[0]:  # Hay una etiqueta al inicio de la linea
                        instruccion = instruccion_ope[1]
                        operandos = instruccion_ope[2:] if len(instruccion_ope) > 1 else []
                        operandos = operandos[0].split(",")
                        comentario = componentes[1].strip() if len(componentes) > 1 else ""
                        # print('La línea "{}" es una linea valida!'.format(linea))
                        # print('La instruccion es: "{}", el o los operadores son: "{}", y el comentario es: "{}"'.
                        # - format(instruccion, operandos, comentario))
                    elif instruccion_ope[1].upper() == "PROC":
                        # Inicia un procedimiento ------------------------------------------------------
                        if pila_llamadas_procedimientos[-1] == '#':  # Si la pila esta vacía, se puede apilar
                            pass
                            # print('La linea "{}" es una linea valida!'.format(linea))  # VALIDA
                            pila_llamadas_procedimientos.append(contador_linea)
                            pila_llamadas_procedimientos.append(instruccion_ope[0])
                        else:
                            # print('Error en el procedimiento: ', instruccion_ope[0])
                            lista_erroes.append(contador_linea)  # Se agrega la linea actual a la lista de errores
                    elif instruccion_ope[1].upper() == "ENDP":
                        # Termina un procedimiento -------------------------------------------------------------
                        if pila_llamadas_procedimientos[-1] != '#':  # Si la pila no esta vacía, se puede desapilar
                            sub_rutina = pila_llamadas_procedimientos.pop()
                            linea_proc = pila_llamadas_procedimientos.pop()
                        if sub_rutina == instruccion_ope[0]:
                            pass
                            # print('La linea "{}" es una linea valida!'.format(linea))  # VALIDA
                        # =============================================================================================
                        elif linea_proc != 0:
                            # print('Error en el procedimiento: ', instruccion_ope[0])
                            lista_erroes.append(linea_proc)
                            lista_erroes.append(contador_linea)  # Se agrega la linea actual a la lista de errores
                            pila_llamadas_procedimientos = ['#']  # Se reinicializa la pila
                    else:
                        # La línea puede tener una instruction, pero no hay una etiqueta válida
                        # print('"{}" no se reconoce (se espera ":" al final de una etiqueta)'.
                        # format(instruccion_ope[0]))
                        lista_erroes.append(contador_linea)  # Se agrega la linea actual a la lista de errores
            elif (linea and linea_vacia != "") and (':' not in instruccion) and ("DEFINE" not in instruccion.upper()):
                linea_comentario = linea_vacia.split()  # No se encontró una instruccion valida.
                if (";" not in linea_comentario[0]) and ("db" not in linea or "dw" not in linea or "DB" not in linea or
                                                         "DW" not in linea):
                    # No se encontró ni un comentario, ni una linea en blanco ni una definicion ni una etiqueta.
                    print(linea, " Sin instruccion")  # INSTRUCCION INVALIDA (RECHAZADA)
                    lista_erroes.append(contador_linea)  # Se agrega la linea actual a la lista de errores
                # Es una línea de definición
                else:
                    pass
                # Hola mundo 

        return lista_erroes
