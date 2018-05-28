from pila import Pila as pila
from Lexico import Lexico as lexico
from numpy import array

class TablaLR:
    def __init__(self):
        self.aceptacion = False
        self.tabla = array([[2,0,0,1],
                            [0,0,-1,0],
                            [0,3,-3,0],
                            [2,0,0,4],
                            [0,0,-2,0]])
        self.columna = ''
        self.fila = ''
        self.accion = 0
        self.contador = 0
        self.reglas = []
        self.numero_elementos = []

    def regresa_tipo(self,simbolo):
        if simbolo == 'Identificador':
            return 0
        elif simbolo == 'Operador de Adicion' or simbolo == 1:
            return 1
        elif simbolo == '$' or simbolo == 2:
            return 2
        elif simbolo == 0:
            return 0
        elif simbolo == 'E' or simbolo == 3:
            return 3
        elif simbolo == 4:
            return 4


    def inicializar_reglas(self):
        self.reglas.append('E')
        self.reglas.append('E')
        self.numero_elementos.append(3)
        self.numero_elementos.append(1)

    def recorrer_entrada(self,cadena,tipos,pila):

        self.inicializar_reglas()
        while self.aceptacion == False:
            print("Cadena: " + str(cadena[self.contador]))
            self.fila = self.regresa_tipo(pila.top())
            self.columna = self.regresa_tipo(tipos[self.contador])
            self.accion = self.tabla[self.fila, self.columna]
            print("Fila: " + str(self.fila)   + " pila_top: " + str(pila.top()))
            print("Columna: " + str(self.columna)   + " tipos__:   " + str(tipos[self.contador]))
            print("Accion: " + str(self.accion))

            if self.accion == -1:
                print("Cadena aceptada")
                self.aceptacion = True
                break
            if self.accion > 0:
                pila.push(tipos[self.contador])
                pila.push(self.accion)
                self.contador = self.contador+1
                pila.muestra()
                print("\n----------------\n\n")
                #if self.contador == 5:
                #    self.aceptacion = True
            elif self.accion < 0:
                self.accion = -self.accion
                self.accion = self.accion-1

                for i in range(self.numero_elementos[self.accion-1]*2):
                    pila.pop()

                self.fila = pila.top()
                pila.push(self.reglas[self.accion-1])
                self.columna = pila.top()
                self.accion = self.tabla[self.fila, self.regresa_tipo(self.columna)]
                pila.push(self.accion)
                print("=====")
                pila.muestra()
                print("=====")
            #    self.aceptacion = True
            else:
                print("Cadena no valida")
                self.aceptacion = True

LR = TablaLR()
p = pila()
lex = lexico

def main():
    entrada = lex.sig_simbolo(lex)
    tipo_entrada = lex.tipos
    p.push('$')
    p.push(0)
    LR.recorrer_entrada(entrada,tipo_entrada,p)


if __name__ == '__main__':
    main()

