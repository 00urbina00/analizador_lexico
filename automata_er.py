import re

class Automata():
    def __init__(self, estados, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = {}
        for estado, expresion_regular, siguiente_estado in transiciones:
            if expresion_regular not in self.transiciones:
                self.transiciones[expresion_regular] = []
            self.transiciones[expresion_regular].append((estado, siguiente_estado))
    
    def acepta_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for caracter in cadena:
            transicion_encontrada = False
            for expresion_regular, transiciones in self.transiciones.items():
                for estado, siguiente_estado in transiciones:
                    if estado == estado_actual and re.match(expresion_regular, caracter):
                        print("Estado actual: " + estado_actual + ", el siguiente estado es: " + siguiente_estado + ", Se ha procesado el caracter: " + caracter)
                        estado_actual = siguiente_estado
                        transicion_encontrada = True
                        break
                if transicion_encontrada:
                    break
            if not transicion_encontrada:
                print("El simbolo actual es: ", caracter, "| terminó")
                return False
        return estado_actual in self.estados_aceptacion
    
# ===========================================================================================================
# Parametros de automata_ds
estados_ds = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14'}
estado_inicial_ds = 'q0'
estados_aceptacion_ds = {'q10', 'q7','q4', 'q5', 'q15', 'q0'}
transiciones_ds = [
    # Transiciones para el nombre de variable
    ('q0', r'[ \t]',        'q0'),      # Espacios indefinidos antes de la variable
    ('q0', r'[a-zA-Z_]',    'q1'),      # Variable (caracteres de la a a la z y guiones bajos)
    ('q1', r'[a-zA-Z0-9_]', 'q1'),      # A partir del segundo caracter tambien se pueden incluir numeros
    ('q1', r'[ \t]',        'q2'),         
    ('q2', r'[ \t]',        'q2'),      # Transición a sí mismo con uno o más espacios o tabulaciones
    
    # Transiciones para el tipo de dato
    
    ('q2', r'[dD]',         'q3'),      # Tipos de datos (d o D)
    ('q3', r'[bBwW]',       'q4'),      # Tipos de datos (b o B o w o W)
    ('q4', r'[ \t]',        'q4'),      # Secuencia indefinida de uno o mas espacios o tabulaciones
    
    # Transiciones para números
    
    ('q4', r'0',            'q5'),      # Se recibe 0, puede ser decimal o inicio de hexadecimal
    # Numeros decimales
    ('q4', r'[0-9]',        'q5'),      # Transición para reconocer el primer digito    numeros
    ('q5', r'[0-9]',        'q5'),      # Secuencia indefinida de digitos               numeros
    ('q5', r',',            'q5'),      # Se lee coma intermedio de 2 numeros
    # Valor indefinido
    ('q4', r'\?',           'q10'),     # Se lee un unico signo de interrogacion como valor indefinido
    # Numeros hexadecimales
    ('q5', r'[xX]',         'q5'),      # Se lee la x como parte del numero hexadecimal seguido del 0
    ('q5', r'[0-9a-fA-F]',  'q5'),      # Secuencia indefinida de dígitos hexadecimales (0-9, a-f, A-F)
    ('q5', r'[ \t]',        'q10'),     # Espacios antes o despues del numero
    ('q5', r'[hH]',         'q15'),     # Lee el sufijo 'h' indicando que es un número hexadecimal
    ('q15', r',',           'q4'),      # Coma para leer otro número hexadecimal
    ('q15', r'[ \t]',       'q15'),     # Lee espacios indefinidos luego de la h
    
    # Transiciones para una cadena
    
    ('q4', r'"',            'q6'),      # Abre comilla para leer una cadena             caracteres
    ('q6', r'[^"]',         'q6'),      # Leer cualquier carácter que no sea una comilla (dentro de las comillas)
    ('q6', r'"',            'q7'),      # Cierra comilla (cadena completa)
    ('q7', r'[ \t]',        'q4'),      # Espacios luego de la cadena
    ('q4', r',',            'q9'),      # Coma luego de los espacios
    ('q7', r',',            'q9'),      # Coma luego de la cadena (sin espacios)
    ('q9', r'[ \t]',        'q9'),      # Espacios indefinidos luego de la coma
    ('q9', r'0',            'q15'),      # Se recibe null al final y se acepta la cadena
    ('q15', r'[0-9a-fA-F]', 'q5'),
    
    # Transiciones para la instruccion dup()
    
    ('q10', r',',           'q4'),     # Si al terminar, encuentra una coma, se mantiene en estado de aceptacion
    ('q10', r'[ \t]',       'q10'),     # Si hay espacios o tabulaciones al final, se acepta la cadena
    
    ('q10', r'[dD]',        'q11'),     # Lee si hay una D o una d
    ('q11', r'[uU]',        'q12'),     # Lee si hay una U o una U
    ('q12', r'[pP]',        'q13'),     # Lee si hay una P o una P
    ('q13', r'[ \t]',       'q4'),      # Lee cualquier espacio o tabulacion antes del parentesis
    ('q13', r'\(',          'q5'),      # Lee si hay un parentesis '('
    ('q4', r'\(',           'q5'),      # Va a leer todos los numeros despues del parentesis
    ('q5', r'\?',           'q14'),     # Lee si hay un signo de interrogacion '?'
    ('q5', r'\)',           'q10'),     # Lee si hay un cierre de parentesis ')' luego de un numero
    ('q14', r'\)',          'q10')      # Lee si hay un cierre de parentesis ')' luego del signo de interrogacion
    
    # Hay un caso de dup("0") en el cual no se reconocen las comillas dentro
    # Hay un caso en que si se usa {variable_a} {operador} offset {variable_b} no se reconocerá
]
# ---------------------------------------------------------------------------------------------------------------
# Parametros de automata_num
estados_num = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5' ,'q6', 'q7', 'q8'}
estado_inicial_num = 'q0'
estados_aceptacion_num = {'q0', 'q1', 'q2', 'q4', 'q6', 'q7', 'q8'}
transiciones_num = [
    # Transiciones para valores vacíos o espacios
    ('q0', r'^$',               'q0'), # Cadena vacía
    ('q0', r'0',                'q4'), # Puede entrar 0x, enteros o letras
    ('q0', r'1',                'q5'), # Entra a los numeros binarios
    ('q0', r'[2-9]',            'q6'), # Reconoce numeros enteros
    ('q5', r'[01]',             'q5'), # Ingresos de numeros binarios
    ('q5', r'[bB]',             'q8'), # Sale de numeros binarios a estado final
    ('q5', r'[a-fA-F]',         'q3'), # Sale de binarios para ir a hexadecimales
    ('q5', r'[2-9]',            'q6'), # Sale de binarios para ir a enteros
    ('q6', r'[0-9]',            'q6'), # Recibe enteros
    ('q6', r'[a-fA-F]',         'q3'), # Sale de enteros a recibir hexadecimal
    ('q3', r'[0-9a-fA-F]',      'q3'), # Se mantiene recibiendo numeros hexadecimales
    ('q3', r'hH',               'q7'), # Salida para aceptacion de hexadecimales
    ('q4', r'[2-9]',            'q6'), # Recibe numeros decimales
    ('q4', r'[01]',             'q5'), # Recibe numeros binarios
    ('q4', r'xX',               'q1'), # Recibe hexa comenzando con 0x
    ('q4', r'[0-9]',            'q2'), # Recibe enteros comenzando 0
    ('q4', r'[A-Fa-f]',         'q3'), # Recibe hexadecimales 0 terminando con h
    ('q1', r'[0-9a-fA-F]',      'q2'), # Recibe hexas 0x
    ('q2', r'[0-9a-fA-F]',      'q2'), # Hexadecimales del tipo 0x
]
# ---------------------------------------------------------------------------------------------------------------
# Parametros de automata_ope
estados_ope = {'q0', 'q1', 'q2', 'q3'}
estado_inicial_ope = 'q0'
estados_aceptacion_ope = {'q0','q2', 'q3'}
transiciones_ope = [
    # Transiciones para valores vacíos o espacios
    ('q0', r'^$',                               'q0'), # Cadena vacía
    ('q0', r'[a-dA-D]',                         'q1'), # Posible ingreso de registro
    ('q0', r'[e-zE-Z_]',                        'q3'), # Entra variable
    ('q1', r'[xhlXHL]',                         'q2'), # Fin de registros
    ('q1', r'[a-gA-Gi-kI-Km-wM-Wy-zY-Z0-9]',    'q3'), # Ingreso de variable
    ('q2', r'[a-zA-Z0-9]',                      'q3'), # Ingreso de variable
    ('q3', r'[a-zA-Z0-9]',                      'q3') # Aceptacion de variables
]