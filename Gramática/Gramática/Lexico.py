import os
from numpy import *


ERROR = -1
IDENTIFICADOR = 0
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
PESOS = 23
BLANCO = 24

def tipo_simbolo(x):
    return {
    IDENTIFICADOR: 'Identificador',
    ENTERO: 'Entero',
    REAL: 'Real',
    CADENA: 'Cadena',
    TIPO: 'Tipo de dato',
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
    _IF_: 'Tipo if',
    _WHILE_: 'Tipo while',
    _RETURN_: 'Tipo return',
    _ELSE_: 'Tipo else',
    PESOS: '$',
    BLANCO: 'Espacio blanco',

    }.get(x,'Error')

class Lexico:
    estado = -1
    cont = 0
    caracter = ""
    continuar = True
    simbolo = ""
    guarda_simbolo = ""
    bandera = False
    punto = False
    cont_punto = 0
    simbolos = []
    tipos = []
    archivo = open("entrada.txt", "r")
    cadena = archivo.read()
    archivo.close()
    caracterNoValido = False

    def sel_tipo(self):
        if self.simbolo == 'if':
            self.aceptacion(self,_IF_)
        elif self.simbolo == 'else':
            self.aceptacion(self, _ELSE_)
        elif self.simbolo == 'while':
            self.aceptacion(self,_WHILE_)
        elif self.simbolo == 'return':
            self.aceptacion(self,_RETURN_)
        elif self.simbolo == 'int' or self.simbolo == 'void' or self.simbolo == 'float':
            #print("Tipo " + self.simbolo)
            self.aceptacion(self,TIPO)
        else:
            #print("Tipo " + self.simbolo)
            self.aceptacion(self, IDENTIFICADOR)

    def fin_archivo(self, estado_x):
        if self.caracter == "":
            self.guarda_simbolo = self.simbolo
        self.proceso_doble(self, estado_x)
        if self.caracter == "":
            self.simbolo = self.guarda_simbolo
        self.guarda_simbolo = ""

    def proceso_doble(self, estado_x):
        self.cont = self.cont -1
        self.aceptacion(self, estado_x)
        self.simbolo = self.simbolo[:len(self.simbolo)-1]

    def sig_estado(self,estado_x):
        if self.caracter!=' ' and self.caracter != '\n' and self.caracter != '\t':
            self.simbolo = self.simbolo + self.caracter
        self.estado = estado_x

    def sig_caracter(self,cadena):
        self.cont = self.cont + 1
        return self.cadena[self.cont-1:self.cont]

    def aceptacion(self,estado_x):
        self.estado = estado_x
        self.simbolo = self.simbolo + self.caracter
        self.continuar = False

    def sig_simbolo(self):
        print("\n")
        print("CADENA: " + self.cadena)
        while(self.cont <= len(self.cadena)):
            if self.cont>0:
                print("SIMBOLO: " + self.simbolo + "      \t\t\tTIPO: " + tipo_simbolo(self.estado))
                self.simbolos.append(self.simbolo)
                self.tipos.append(tipo_simbolo(self.estado))


            self.continuar = True
            self.simbolo = ""
            self.estado = -1
            self.guarda_simbolo = ""
            self.punto = False
            self.cont_punto = 0

            while(self.continuar):
                self.caracter = ""
                self.caracter = Lexico.sig_caracter(self,self.cadena)
                if self.estado == -1:
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
                    elif self.caracter == '=':
                        self.sig_estado(self,IGUAL)
                    elif self.caracter == '<' or self.caracter == '>':
                        self.sig_estado(self,OP_REL)
                    elif self.caracter == '!':
                        self.sig_estado(self,OP_NOT)
                    elif self.caracter == '&':
                        self.sig_estado(self,OP_AND)
                    elif self.caracter == '|':
                        self.sig_estado(self, OP_OR)
                    elif self.caracter.isalpha() or self.caracter == '_':
                        self.sig_estado(self,IDENTIFICADOR)
                    elif self.caracter.isdigit():
                        self.sig_estado(self,ENTERO)
                    elif self.caracter == " " or self.caracter == '\n' or self.caracter == '\t':
                        self.sig_estado(self,-1)
                    else:
                        self.aceptacion(self,-1)
                elif self.estado == IGUAL:
                    if self.caracter != '=':
                        self.fin_archivo(self, IGUAL)
                    elif self.caracter == '=':
                        self.aceptacion(self, OP_IGUALDAD)
                elif self.estado == OP_REL:
                    if self.caracter != '=':
                        self.fin_archivo(self,OP_REL)
                    elif self.caracter == '=':
                        self.aceptacion(self,OP_REL)
                elif self.estado == OP_NOT:
                    if self.caracter != '=':
                        self.fin_archivo(self,OP_NOT)
                    elif self.caracter == '=':
                        self.aceptacion(self, OP_REL)
                elif self.estado == OP_AND:
                    if self.caracter != '&':
                        self.fin_archivo(self,-1)
                    elif self.caracter == '&':
                        self.aceptacion(self,OP_AND)
                elif self.estado == OP_OR:
                    if self.caracter != '|':
                        self.fin_archivo(self,-1)
                    elif self.caracter == '|':
                        self.aceptacion(self,OP_OR)
                elif self.estado == ENTERO:
                    self.guarda_simbolo = self.simbolo
                    if self.caracter.isdigit() or self.caracter == '.':
                        if self.caracter == '.':
                            self.punto = True
                            self.cont_punto = self.cont_punto +1
                        if self.cont_punto == 2:
                            self.proceso_doble(self,REAL)

                        else:
                            self.sig_estado(self,ENTERO)
                    elif self.punto == True:
                        #print(self.guarda_simbolo)
                        self.simbolo = self.guarda_simbolo
                        self.proceso_doble(self,REAL)
                        #self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        #print(self.simbolo[len(self.simbolo)-1:len(self.simbolo)])
                        if self.simbolo[len(self.simbolo)-1:len(self.simbolo)] == '.':
                            self.cont = self.cont -1
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                    else:
                        self.fin_archivo(self,ENTERO)
                        #self.proceso_doble(self,ENTERO)
                        #print("SIM_ " + self.simbolo)
                        self.punto = False

                elif self.estado == IDENTIFICADOR:
                    self.cont = self.cont - 1
                    self.guarda_simbolo = self.caracter
                    self.caracter = self.sig_caracter(self, self.cadena)
                    if self.caracter.isdigit() or self.caracter.isalpha() or self.caracter == '_':
                        self.simbolo = self.simbolo[:len(self.simbolo)]
                        self.sig_estado(self, IDENTIFICADOR)
                    else:
                        if self.caracter == "":
                            self.guarda_simbolo = self.simbolo
                        self.sel_tipo(self)
                        self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        self.cont = self.cont - 1
                        if self.caracter == "":
                            self.simbolo = self.guarda_simbolo
                        self.guarda_simbolo = ""
                else:
                    self.continuar = False
                    self.estado = -1

        print("\n\n")
        self.simbolos.append('$')
        self.tipos.append('$')
        return self.simbolos
