import re

class Automata_Var():
    def __init__(self, estados, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = {}
        for estado, expresion_regular, siguiente_estado in transiciones:
            self.transiciones[(estado, expresion_regular)] = siguiente_estado

    def acepta_cadena_caracter(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            transicion_encontrada = False
            for transicion, siguiente_estado in self.transiciones.items():
                estado, expresion_regular = transicion
                if estado == estado_actual and re.match(expresion_regular, simbolo):
                    estado_actual = siguiente_estado
                    transicion_encontrada = True
                    break
            if not transicion_encontrada:
                return False
        return estado_actual in self.estados_aceptacion


estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8','q9',
           'q10','q11','q12','q13','q14','q15','q16','q17','q18','q19',
           'q20','q21','q22','q23'}
estado_inicial = 'q0'
estados_aceptacion = {'q15','q19','q20','q21','q23'}
transiciones = {
    ('q0', 'd', 'q1'),
    ('q1', r'[w|b]', 'q2'),
    ('q2', ' ', 'q3'),
    ('q3', r'[0-9]', 'q4'),
    ('q3', '"', 'q18'),
    ('q4', r'[0-9]', 'q4'),
    ('q4', ' ', 'q5'),
    ('q5', 'd','q6'),
    ('q6', 'u', 'q7'),
    ('q7', 'p', 'q8'),
    ('q8', ' ', 'q9'),
    ('q9', '(', 'q10'),
    ('q10', '0', 'q11'),
    ('q10', '"', 'q17'),
    ('q11', 'x', 'q12'),
    ('q11', r'[a-f0-9]', 'q16'),
    ('q12', r'[0-9a-f]', 'q13'),
    ('q13', r'[0-9a-f]', 'q13'),
    ('q13', 'h', 'q14'),
    ('q14', ')', 'q15'),
    ('q16', r'[a-f0-9]', 'q16'),
    ('q16', 'h', 'q14'),
    ('q17', r'[a-z0-9]', 'q17'),
    ('q17', '"', 'q14'),
    ('q18', r'[a-z0-9\s]', 'q18'),
    ('q18', '"', 'q19'),
    ('q19', ',', 'q20'),
    ('q20', '"', 'q18'),
    ('q20', ' ', 'q20'),
    ('q20', '0', 'q21'),
    ('q21', r'[d|a]', 'q22'),
    ('q22', 'h', 'q23'),
    ('q23', ',', 'q20')
}

automata = Automata_Var(estados, estado_inicial, estados_aceptacion, transiciones)

cadena = input("Ingrese una cadena: ")
if automata.acepta_cadena_caracter(cadena.lower()):
    print("La cadena es válida para el autómata.")
else:
    print("La cadena no es válida para el autómata.")