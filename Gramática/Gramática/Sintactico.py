import numpy as np
from Arbol import Arbol as trees

tree = trees()
class TablaLR:
    def __init__(self):
        self.aceptacion = False
        #self.tabla = np.array([])
        self.tabla = np.zeros((95,46))
        self.columna = ''
        self.fila = ''
        self.accion = 0
        self.contador = 0
        self.reglas = []
        self.numero_elementos = []
        self.numero_regla = []
        self.codigo = []
        self.arbol = []
        self.correcto = False

    def regresa_tipo(self,simbolo):

        simbolo = str(simbolo)

        if simbolo.isdigit():
            return int(simbolo)
        if simbolo == 'Identificador':
            return 0
        elif simbolo == 'Entero':
            return 1
        elif simbolo == 'Real':
            return 2
        elif simbolo == 'Cadena':
            return 3
        elif simbolo == 'Tipo de dato':
            return 4
        elif simbolo == 'Operador de Adicion':
            return 5
        elif simbolo == 'Operador de Multiplicacion':
            return 6
        elif simbolo == 'Operador Relacional':
            return 7
        elif simbolo == 'Operador OR':
            return 8
        elif simbolo == 'Operador AND':
            return 9
        elif simbolo == 'Operador NOT':
            return 10
        elif simbolo == 'Operador de Igualdad':
            return 11
        elif simbolo == 'Punto y coma':
            return 12
        elif simbolo == 'Coma':
            return 13
        elif simbolo == 'Parentesis que abre':
            return 14
        elif simbolo == 'Parentesis que cierra':
            return 15
        elif simbolo == 'Corchete que abre':
            return 16
        elif simbolo == 'Corchete que cierra':
            return 17
        elif simbolo == 'Igual':
            return 18
        elif simbolo == 'Tipo if':
            return 19
        elif simbolo == 'Tipo while':
            return 20
        elif simbolo == 'Tipo return':
            return 21
        elif simbolo == 'Tipo else':
            return 22
        elif simbolo == '$':
            return 23
        elif simbolo == 'programa':
            return 24
        elif simbolo == 'Definiciones':
            return 25
        elif simbolo == 'Definicion':
            return 26
        elif simbolo == 'DefVar':
            return 27
        elif simbolo == 'ListaVar':
            return 28
        elif simbolo == 'DefFunc':
            return 29
        elif simbolo == 'Parametros':
            return 30
        elif simbolo == 'ListaParam':
            return 31
        elif simbolo == 'BloqFunc':
            return 32
        elif simbolo == 'DefLocales':
            return 33
        elif simbolo == 'DefLocal':
            return 34
        elif simbolo == 'Sentencias':
            return 35
        elif simbolo == 'Sentencia':
            return 36
        elif simbolo == 'Otro':
            return 37
        elif simbolo == 'Bloque':
            return 38
        elif simbolo == 'ValorRegresa':
            return 39
        elif simbolo == 'Argumentos':
            return 40
        elif simbolo == 'ListaArgumentos':
            return 41
        elif simbolo == 'Termino':
            return 42
        elif simbolo == 'LlamadaFunc':
            return 43
        elif simbolo == 'SentenciaBloque':
            return 44
        elif simbolo == 'Expresion':
            return 45

    def inicializar_reglas(self):
        archivo = open("reglas.txt","r")
        cadena = archivo.read()
        archivo.close()
        datos = cadena.split('*')
        numero_reglas = datos[0]
        reglas = datos[1].split('|')
        for i in range(int(numero_reglas)):
            datos_regla = reglas[i].split('-')
            self.numero_regla.append(int(datos_regla[0]))
            self.numero_elementos.append(int(datos_regla[1]))
            self.reglas.append(datos_regla[2])

    def cargar_tabla(self):
        archivo = open("tabla.txt","r")
        cadena = archivo.read()
        archivo.close()

        cadena = cadena.split('*')
        medidas = cadena[0].split('|')
        filas = medidas[0]
        columnas = medidas[1]
        row = cadena[1].split('\n')
        row.pop(0)
        #self.tabla = np.zeros((int(filas),int(columnas)))

        for i in range(int(filas)):
            col = row[i].split('\t')
            for j in range(int(columnas)):
                self.tabla[i,j]=int(col[j])

    def recorrer_entrada(self,cadena,tipos,pila,pila_codigo):
        self.inicializar_reglas()
        self.cargar_tabla()
        pila_codigo.push
        while self.aceptacion == False:
            #print("CADENA " + str(cadena[self.contador]))
            self.fila = self.regresa_tipo(pila.top())
            #print(tipos[self.contador])
            self.columna = self.regresa_tipo(tipos[self.contador])
            self.accion = self.tabla[self.fila, self.columna]
            #print("Fila: " + str(self.fila)   + " pila_top: " + str(pila.top()))
            #print("Columna: " + str(self.columna)   + " tipos__:   " + str(tipos[self.contador]))
            #print("Accion: " + str(self.accion))

            if self.accion == -1:
                #print("Accion: " + str(self.accion))
                #print("Cadena aceptada")
                self.aceptacion = True
                self.correcto = True
                return tree
                break
            if self.accion > 0:
                #print("Accion: " + str(self.accion))
                pila.push(tipos[self.contador])
                pila.push(int(self.accion))
                ######################################################
                pila_codigo.push(str(cadena[self.contador]))
                pila_codigo.push(int(self.accion))
                ######################################################
                self.contador = self.contador+1
                #pila.muestra()
                #print("\n----------------\n\n")
            elif self.accion < 0:
                self.accion = -self.accion
                self.accion = self.accion-1
                #print("Accion negativa: " + str(self.accion))
                #print(self.accion)
                #print(len(self.numero_elementos))

                tree.forma_arbol(pila,pila_codigo,self.numero_elementos,self.accion)
                #if self.reglas[int(self.accion)-1] not in self.arbol:
                self.arbol.append(self.reglas[int(self.accion)-1])
                #for i in range(self.numero_elementos[int(self.accion)-1]*2):
                #    pila.pop()

                self.accion = int(self.accion)

                self.fila = pila.top()
                #print("Fila" + str(self.fila))
                self.accion = int(self.accion)
                pila.push(self.reglas[self.accion-1])
                ######################################################
                pila_codigo.push(self.reglas[self.accion-1])
                ######################################################
                #print("Columna: " + str(self.regresa_tipo(pila.top())))
                self.columna = pila.top()
                #print("----- " + str(self.regresa_tipo(self.columna)))
                self.accion = self.tabla[self.fila, self.regresa_tipo(self.columna)]
                #print("Accion" + str(self.accion))
                pila.push(int(self.accion))
                ######################################################
                pila_codigo.push(int(self.accion))
                ######################################################
                #print("Hi- ": + str(self.reglas[int(self.accion)]))
                #pila.push(self.reglas[int(self.accion)])
                #pila.push(int(self.accion))
                #pila.muestra()
                #print("\n----------------\n\n")
            else:
                #print("Cadena no valida")
                self.aceptacion = True
                self.correcto = False
