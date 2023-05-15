# Transiciones 
# [[0, 'x', 1],[1, '', -1]]
# Estados
# []

class Automata():
    def __init__(self, estados, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones

    def acepta_cadena(self, cadena):
        estado_actual = self.estado_inicial

        for simbolo in cadena:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = self.transiciones[(estado_actual, simbolo)]
            else:
                return False

        return estado_actual in self.estados_aceptacion


# Ejemplo de uso
estados = {'q0', 'q1', 'q2'}
estado_inicial = 'q0'
estados_aceptacion = {'q2'}
transiciones = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q0',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2'
}

automata = Automata(estados, estado_inicial, estados_aceptacion, transiciones)

cadena1 = '001'
cadena2 = '110'

print(automata.acepta_cadena(cadena1))  # True
print(automata.acepta_cadena(cadena2))  # False