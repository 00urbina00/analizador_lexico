import re

class Automata():
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


estados = {'q0', 'q1', 'q2', 'q3','q4'}
estado_inicial = 'q0'
estados_aceptacion = {'q1','q2','q3','q4'}
transiciones = {
    ('q0', '0', 'q1'),
    ('q0', r'[1-9]', 'q4'),
    ('q1', 'x', 'q2'),
    ('q1', r'[0-9]', 'q4'),
    ('q2', r'[0-9a-f]', 'q2'),
    ('q2', 'h', 'q3'),
    ('q4', r'[0-9a-f]', 'q4'),
    ('q4', 'h','q3')
}

automata = Automata(estados, estado_inicial, estados_aceptacion, transiciones)

cadena = input("Ingrese una cadena: ")
if automata.acepta_cadena_caracter(cadena):
    print("La cadena es válida para el autómata.")
else:
    print("La cadena no es válida para el autómata.")