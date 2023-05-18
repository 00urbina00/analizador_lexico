class Automata_Var():
    def __init__(self, estados, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones
    
    def acepta_cadena_caracter(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = self.transiciones[(estado_actual, simbolo)]
            else:
                return False
        return estado_actual in self.estados_aceptacion
    
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8','q9',
           'q10','q11','q12','q13','q14','q15','q16','q17','q18','q19',
           'q20','q21','q22','q23'}
estado_inicial = 'q0'
estados_aceptacion = {'q15','q19','q20','q21','q23'}
transiciones = {
    ('q0', 'd'): 'q1',
    
    ('q1', 'w'): 'q2',
    ('q1', 'b'): 'q2',
    
    ('q2', ' '): 'q3',

    ('q3', '0'): 'q4',
    ('q3', '1'): 'q4',
    ('q3', '2'): 'q4',
    ('q3', '3'): 'q4',
    ('q3', '4'): 'q4',
    ('q3', '5'): 'q4',
    ('q3', '6'): 'q4',
    ('q3', '7'): 'q4',
    ('q3', '8'): 'q4',
    ('q3', '9'): 'q4',
    ('q3', '"'): 'q18',

    ('q4', '0'): 'q4',
    ('q4', '1'): 'q4',
    ('q4', '2'): 'q4',
    ('q4', '3'): 'q4',
    ('q4', '4'): 'q4',
    ('q4', '5'): 'q4',
    ('q4', '6'): 'q4',
    ('q4', '7'): 'q4',
    ('q4', '8'): 'q4',
    ('q4', '9'): 'q4',
    ('q4', ' '): 'q5',

    ('q5', 'd'): 'q6',

    ('q6', 'u'): 'q7',

    ('q7', 'p'): 'q8',

    ('q8', ' '): 'q9',

    ('q9', '('): 'q10',

    ('q10', '0'): 'q11',
    ('q10', '"'): 'q17',

    ('q11', 'x'): 'q12',
    ('q11', 'a'): 'q16',
    ('q11', 'b'): 'q16',
    ('q11', 'c'): 'q16',
    ('q11', 'd'): 'q16',
    ('q11', 'e'): 'q16',
    ('q11', 'f'): 'q16',
    ('q11', '0'): 'q16',
    ('q11', '1'): 'q16',
    ('q11', '2'): 'q16',
    ('q11', '3'): 'q16',
    ('q11', '4'): 'q16',
    ('q11', '5'): 'q16',
    ('q11', '6'): 'q16',
    ('q11', '7'): 'q16',
    ('q11', '8'): 'q16',
    ('q11', '9'): 'q16',

    ('q12', '0'): 'q13',
    ('q12', '1'): 'q13',
    ('q12', '2'): 'q13',
    ('q12', '3'): 'q13',
    ('q12', '4'): 'q13',
    ('q12', '5'): 'q13',
    ('q12', '6'): 'q13',
    ('q12', '7'): 'q13',
    ('q12', '8'): 'q13',
    ('q12', '9'): 'q13',
    ('q12', 'a'): 'q13',
    ('q12', 'b'): 'q13',
    ('q12', 'c'): 'q13',
    ('q12', 'd'): 'q13',
    ('q12', 'e'): 'q13',
    ('q12', 'f'): 'q13',

    ('q13', '0'): 'q13',
    ('q13', '1'): 'q13',
    ('q13', '2'): 'q13',
    ('q13', '3'): 'q13',
    ('q13', '4'): 'q13',
    ('q13', '5'): 'q13',
    ('q13', '6'): 'q13',
    ('q13', '7'): 'q13',
    ('q13', '8'): 'q13',
    ('q13', '9'): 'q13',
    ('q13', 'a'): 'q13',
    ('q13', 'b'): 'q13',
    ('q13', 'c'): 'q13',
    ('q13', 'd'): 'q13',
    ('q13', 'e'): 'q13',
    ('q13', 'f'): 'q13',
    ('q13', 'h'): 'q14',

    ('q14', ')'): 'q15',

    ('q16', 'a'): 'q16',
    ('q16', 'b'): 'q16',
    ('q16', 'c'): 'q16',
    ('q16', 'd'): 'q16',
    ('q16', 'e'): 'q16',
    ('q16', 'f'): 'q16',
    ('q16', '0'): 'q16',
    ('q16', '1'): 'q16',
    ('q16', '2'): 'q16',
    ('q16', '3'): 'q16',
    ('q16', '4'): 'q16',
    ('q16', '5'): 'q16',
    ('q16', '6'): 'q16',
    ('q16', '7'): 'q16',
    ('q16', '8'): 'q16',
    ('q16', '9'): 'q16',
    ('q16', 'h'): 'q14',

    ('q17', 'a'):  'q17',
    ('q17', 'b'):  'q17',
    ('q17', 'c'):  'q17',
    ('q17', 'd'):  'q17',
    ('q17', 'e'):  'q17',
    ('q17', 'f'):  'q17',
    ('q17', 'g'):  'q17',
    ('q17', 'h'):  'q17',
    ('q17', 'i'):  'q17',
    ('q17', 'j'):  'q17',
    ('q17', 'k'):  'q17',
    ('q17', 'l'):  'q17',
    ('q17', 'm'):  'q17',
    ('q17', 'n'):  'q17',
    ('q17', 'o'):  'q17',
    ('q17', 'p'):  'q17',
    ('q17', 'q'):  'q17',
    ('q17', 'r'):  'q17',
    ('q17', 's'):  'q17',
    ('q17', 't'):  'q17',
    ('q17', 'u'):  'q17',
    ('q17', 'v'):  'q17',
    ('q17', 'w'):  'q17',
    ('q17', 'x'):  'q17',
    ('q17', 'y'):  'q17',
    ('q17', 'z'):  'q17',
    ('q17', '0'):  'q17',
    ('q17', '1'):  'q17',
    ('q17', '2'):  'q17',
    ('q17', '3'):  'q17',
    ('q17', '4'):  'q17',
    ('q17', '5'):  'q17',
    ('q17', '6'):  'q17',
    ('q17', '7'):  'q17',
    ('q17', '8'):  'q17',
    ('q17', '9'):  'q17',
    ('q17', '"'):  'q14',
    
    ('q18', ' '):  'q18',
    ('q18', 'a'):  'q18',
    ('q18', 'b'):  'q18',
    ('q18', 'c'):  'q18',
    ('q18', 'd'):  'q18',
    ('q18', 'e'):  'q18',
    ('q18', 'f'):  'q18',
    ('q18', 'g'):  'q18',
    ('q18', 'h'):  'q18',
    ('q18', 'i'):  'q18',
    ('q18', 'j'):  'q18',
    ('q18', 'k'):  'q18',
    ('q18', 'l'):  'q18',
    ('q18', 'm'):  'q18',
    ('q18', 'n'):  'q18',
    ('q18', 'o'):  'q18',
    ('q18', 'p'):  'q18',
    ('q18', 'q'):  'q18',
    ('q18', 'r'):  'q18',
    ('q18', 's'):  'q18',
    ('q18', 't'):  'q18',
    ('q18', 'u'):  'q18',
    ('q18', 'v'):  'q18',
    ('q18', 'w'):  'q18',
    ('q18', 'x'):  'q18',
    ('q18', 'y'):  'q18',
    ('q18', 'z'):  'q18',
    ('q18', '0'):  'q18',
    ('q18', '1'):  'q18',
    ('q18', '2'):  'q18',
    ('q18', '3'):  'q18',
    ('q18', '4'):  'q18',
    ('q18', '5'):  'q18',
    ('q18', '6'):  'q18',
    ('q18', '7'):  'q18',
    ('q18', '8'):  'q18',
    ('q18', '9'):  'q18',
    ('q18', '"'):  'q19',

    ('q19', ','):   'q20',

    ('q20', '"'):   'q18',
    ('q20', ' '):   'q20',
    ('q20', '0'):   'q21',

    ('q21', 'd'):   'q22',
    ('q21', 'a'):   'q22',

    ('q22', 'h'):   'q23',
    ('q23', ','):   'q20'
}

automata = Automata_Var(estados, estado_inicial, estados_aceptacion, transiciones)

cadena1 = 'db "hola cadena12", 0ah'

print(automata.acepta_cadena_caracter(cadena1))