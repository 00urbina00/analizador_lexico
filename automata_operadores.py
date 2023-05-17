import re
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

    def acepta_cadena_caracter(self, cadena):
        estado_actual = self.estado_inicial

        for simbolo in cadena:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = self.transiciones[(estado_actual, simbolo)]
            else:
                return False

        return estado_actual in self.estados_aceptacion
    def acepta_cadena(self, cadena):
        estado_actual = self.estado_inicial

        for simbolo in cadena:
            siguiente_estado = None
            for transicion in self.transiciones:
                origen, destino = transicion
                if re.match(origen, simbolo):
                    siguiente_estado = destino
                    break
            
            if siguiente_estado is None:
                return False

            estado_actual = siguiente_estado

        return estado_actual in self.estados_aceptacion

# Ejemplo de uso
estados = {'q0', 'q1', 'q2'}
estado_inicial = 'q0'
estados_aceptacion = {'q2'}
transiciones = {
    (r'[0-9]', 'q1'),
    (r'[a-z]', 'q0'),
    (r'[A-Z]', 'q0')
}

# automata = Automata(estados, estado_inicial, estados_aceptacion, transiciones)

cadena1 = 'aB3'
cadena2 = '123'
cadena3 = 'AbC'

# print(automata.acepta_cadena(cadena1))  # True
# print(automata.acepta_cadena(cadena2))  # False
# print(automata.acepta_cadena(cadena3))  # False

"""
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

print(automata.acepta_cadena_caracter(cadena1))  # True
print(automata.acepta_cadena_caracter(cadena2))  # False

"""

bloque_de_texto = """
linea        db      1 dup (0)
n_arch       db      80 dup (0)
han_n_a      dw      0
han_n_a_escr dw      0
salir        db      0
t_linea      db      0   
error        dw      0          
NvaLine      db      0dh,0ah 
msg1         db      "Dame el nombre del archivo de texto a abrir. usa el formato 8.3", 0
error01      db      "Funcion No Valida",0
error02      db      "Archivo No Encontrado",0
error03      db      "Ruta No Valida",0
error04      db      "Handle No Disponible",0
error05      db      "Acceso Denegado",0
error06      db      "Handle no valido",0
error07      db      "Excede el numero de caracteres",0
 
enter        db      "", 0dh,0aH
espacio      db      " "
contador     dw      0  
bcd8421      db      5   dup (?)
bcdA         db      5   dup ("0")
name_new     db      80  dup (0)
tam_bcdA     db      name_new - offset bcdA
tam_blan     db      contador - offset espacio
tam_enter    db      espacio - offset enter
msg2         db      "La ruta tiene un maximo de 80 caracteres",0
tam_msg2     db      tam_msg2 - offset msg2
msg3         db      "Dame el nombre del archivo de salida. usa el formato 8.3", 0
nombre       db      "",0dH,0aH
msg_fin      db      "Archivo creado con exito!", 0
"""
# Uso para procesar el bloque de texto
# patron_variable = r"([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z]+)\s+(\".*?\"|\S+)(?:\s*\[[^\]]*\])?"

lineas = bloque_de_texto.strip().split("\n")

for linea in lineas:
    # re para procesar lineas de texto
    resultado = re.match(r"(\w+)\s+([a-zA-Z_]+)\s+(.*)", linea)
    if resultado:
        nombre_variable = resultado.group(1)
        tipo_dato = resultado.group(2)
        definicion = resultado.group(3).strip()
        print(f"Nombre de variable: {nombre_variable}")
        print(f"Tipo de dato: {tipo_dato}")
        print(f"Definición: {definicion}")
        print(" --------------------------------------")