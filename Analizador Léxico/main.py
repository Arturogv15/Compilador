'''Seminario de Solución de Problemas de Traductores de Lenguajes II
 *Analizador léxico del compilador
 *Arturo Guzmán Vázquez'''
import os

ERROR = 0
IDENTIFICADOR = 24
ENTERO = 1
REAL = 2
CADENA = 3
TIPO = 4
OP_AD = 5
OP_MULTI = 6
OP_REL = 7
OP_OR = 8
OP_AND = 9
OP_NOT = 10
OP_IGUALDAD = 11
PUNTO_Y_COMA = 12
COMA = 13
PAR_ABRE = 14
PAR_CIERRE = 15
COR_ABRE = 16
COR_CIERRE = 17
IGUAL = 18
_IF_ = 19
_WHILE_ = 20
_RETURN_ = 21
_ELSE_ = 22
_PESOS_ = 23

def tipo_simbolo(x):
    return {
    IDENTIFICADOR: 'Identificador',
    ENTERO: 'Entero',
    REAL: 'Real',
    CADENA: 'Cadena',
    TIPO: 'Tipo',
    OP_AD: 'Operador de Adicion',
    OP_MULTI: 'Operador de Multiplicacion',
    OP_REL: 'Operador Relacional',
    OP_OR: 'Operador OR',
    OP_AND: 'Operador AND',
    OP_NOT: 'Operador NOT',
    OP_IGUALDAD: 'Operador de Igualdad',
    PUNTO_Y_COMA: 'Punto y coma',
    COMA: 'Coma',
    PAR_ABRE: 'Parentesis que abre',
    PAR_CIERRE: 'Parentesis que cierra',
    COR_ABRE: 'Corchete que abre',
    COR_CIERRE: 'Corchete que cierra',
    IGUAL: 'Igual',
    _IF_: 'if',
    _WHILE_: 'while',
    _RETURN_: 'return',
    _ELSE_: 'else',
    _PESOS_: 'pesos'
    }.get(x,'Error')

class Lexico:
    estado = 0
    cont = 0
    caracter = ""
    continuar = True
    simbolo = ""
    cadena = "+-)(+g63f6}} {*)987.;odf,"
    flag = False
    num_flag = 0

    def sigEstado(self,estado_x):
        self.simbolo = self.simbolo + self.caracter
        self.estado = estado_x

    def sigCaracter(self,cadena):
        self.cont = self.cont + 1

        return self.cadena[self.cont-1:self.cont]

    def aceptacion(self,estado_x):
        self.estado = estado_x
        self.continuar = False

    def sigSimbolo(self):
        while(self.cont < len(self.cadena)):
            self.continuar = True
            self.estado = 0
            while(self.continuar):
                self.caracter = Lexico.sigCaracter(self,self.cadena)

                if self.estado == 0:
                    if self.caracter == ',':
                        self.aceptacion(self,COMA)
                    elif self.caracter == ';':
                        self.aceptacion(self,PUNTO_Y_COMA)
                    elif self.caracter == ')':
                        self.aceptacion(self,PAR_CIERRE)
                    elif self.caracter == '(':
                        self.aceptacion(self,PAR_ABRE)
                    elif self.caracter == '{':
                        self.aceptacion(self,COR_ABRE)
                    elif self.caracter == '}':
                        self.aceptacion(self,COR_CIERRE)
                    elif self.caracter == '+' or self.caracter == '-':
                        self.aceptacion(self,OP_AD)
                    elif self.caracter == '/' or self.caracter == '*':
                        self.aceptacion(self,OP_MULTI)

                print("SIMBOLO: " + self.caracter + "    TIPO: " + tipo_simbolo(self.estado)+ "\n\n")
Cl = Lexico
Cl.sigSimbolo(Cl)
