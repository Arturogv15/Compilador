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
BLANCO = 23

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
    BLANCO: 'Espacio blanco',

    }.get(x,'Error')

class Lexico:
    estado = 0
    cont = 0
    caracter = ""
    continuar = True
    simbolo = ""
    #cadena = "\"+-)===(=<+g63f=!=&!==={&&{>!!6}} {*)98<=7.|;/&&||od&f,"
    cadena = "*-_¿f*oat34&&_=di()* w$#%32) nf_t--)==&&&--_dfg45e34t*a"
    guarda_simbolo = ""

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
        print("\n\n")
        print("CADENA: " + self.cadena + "\n")
        while(self.cont <= len(self.cadena)):
            if self.cont>0:
                print("SIMBOLO: " + self.simbolo + " \t\t\tTIPO: " + tipo_simbolo(self.estado))
            self.continuar = True
            self.simbolo = ""
            self.estado = 0
            self.guarda_simbolo = ""

            while(self.continuar):
                self.caracter = ""
                self.caracter = Lexico.sig_caracter(self,self.cadena)
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
                    elif self.caracter == " ":
                        self.aceptacion(self,BLANCO)
                    else:
                        self.aceptacion(self,0)
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
                        self.fin_archivo(self,0)
                    elif self.caracter == '&':
                        self.aceptacion(self,OP_AND)
                elif self.estado == OP_OR:
                    if self.caracter != '|':
                        self.fin_archivo(self,0)
                    elif self.caracter == '|':
                        self.aceptacion(self,OP_OR)
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
                        self.aceptacion(self, IDENTIFICADOR)
                        self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        self.cont = self.cont - 1
                        if self.caracter == "":
                            self.simbolo = self.guarda_simbolo
                        self.guarda_simbolo = ""
                else:
                    self.continuar = False
                    self.estado = 0



        print("\n\n")

Cl = Lexico
Cl.sig_simbolo(Cl)






'''


                    #    print("Final " +self.simbolo)
                        #self.cont = self.cont -1
                        if self.simbolo == 'if':
                            self.aceptacion(self, _IF_)
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        elif self.simbolo == 'while':
                            self.aceptacion(self,_WHILE_)
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        elif self.simbolo == 'return':
                            self.aceptacion(self,_RETURN_)
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        elif self.simbolo == 'else':
                            self.aceptacion(self, _ELSE_)
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        elif self.simbolo == 'int' or self.simbolo == 'float' or self.simbolo == 'void':
                            self.aceptacion(self,TIPO)
                            self.simbolo = self.simbolo[:len(self.simbolo)-1]
                        else:
                    #    self.simbolo = self.simbolo[:len(self.simbolo)-1]
                    #    self.aceptacion(self, IDENTIFICADOR)
                        self.proceso_doble(self,IDENTIFICADOR)
                        self.flag_alfa = False '''




'''    elif self.estado == ENTERO:
        if self.caracter.isdigit() == False and self.caracter != '.':
            if len(self.guarda_simbolo) == 0:
                self.proceso_doble(self,ENTERO)
            elif len(self.guarda_simbolo) > 0 and self.flag == True:
                self.proceso_doble(self,REAL)
        elif self.caracter.isdigit():
            if self.flag != True or len(self.guarda_simbolo)>0:
                self.simbolo = self.guarda_simbolo
                self.flag = True
            self.caracter = self.sig_caracter(self,self.cadena)
            self.sig_estado(self,ENTERO)
        elif self.caracter == '.':
            self.guarda_simbolo = self.simbolo
            self.caracter = self.sig_caracter(self,self.cadena)
            self.sig_estado(self,ENTERO)'''
