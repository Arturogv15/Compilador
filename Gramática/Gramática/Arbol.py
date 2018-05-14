PROGRAMA = 0                                #
DEFINICIONES_V = 1                          #
DEFINICIONES = 2                            #
DEFINICION_VAR = 3
DEFINICION_FUN = 4                          #
DEFVAR = 5
LISTAVAR_V = 6
LISTAVAR = 7
DEFFUN = 8                                  #
PARAMETROS_V = 9                            #
PARAMETROS = 10                             #
LISTAPARAM_V = 11
LISTAPARAM = 12
BLOQFUNC = 13                               #
DEFLOCALES_V = 14
DEFLOCALES = 15
DEFLOCAL_VAR = 16
DEFLOCAL_SENT = 17
SENTENCIAS_V = 18
SENTENCIAS = 19
SENTENCIA_ASIG = 20
SENTENCIA_IF = 21
SENTENCIA_WHILE = 22
SENTENCIA_RETURN = 23
SENTENCIA_CALLFUN = 24
OTRO_V = 25
OTRO = 26
BLOQUE = 27
VALORREGRESA_V = 28
VALORREGRESA = 29
ARGUMENTOS_V = 30
ARGUMENTOS = 31
LISTAARGUMENTOS_V = 32
LISTAARGUMENTOS = 33
TERMINO_CALLFUN = 34
TERMINO_ID = 35
TERMINO_INT = 36
TERMINO_REAL = 37
TERMINO_CAD = 38
LLAMADAFUN = 39
SENTENCIABLOQUE_SENT = 40
SENTENCIABLOQUE_BLOQ = 41
EXPRESION = 42
EXPRESION_MAS = 43
EXPRESION_NOT = 44
EXPRESION_PLUS = 45
EXPRESION_MULT = 46
EXPRESION_REL = 47
EXPRESION_IGUAL = 48
EXPRESION_AND = 49
EXPRESION_OR = 50
EXPRESION_TERMINO = 51

class Expresion():
    def __init__(self,Termino,Expresion1,Expresion2):
        self.termino = Termino
        self.expresion1 = Expresion1
        self.expresion2 = Expresion2

class ListaArgumentos(Expresion):
    def __init__(self,Expresion,ListaArgumentos):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos

class Argumentos(ListaArgumentos):
    def __init__(self,ListaArgumentos,Expresion):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos

class LlamadaFuncion(Argumentos):
    def __init__(self,Argumentos):
        self.identificador = identificador
        self.argumentos = Argumentos

class Termino(LlamadaFuncion):
    def __init__(self,id,entero,real,cadena,LlamadaFuncion):
        self.identificador = id
        self.entero = entero
        self.real = real
        self.cadena = cadena
        self.llamada_funcion = LlamadaFuncion


class ValorRegresa(Expresion):
    def __init__(self,Expresion):
        self.vacio = None
        self.expresion = Expresion


class Sentencia(Expresion):
    def __init__(self,identificador,Expresion,SentenciaBloque,Otro,Bloque,ValorRegresa,LlamadaFuncion):
        self.identificador = identificador
        self.expresion = Expresion
        self.sentencia_bloque = SentenciaBloque
        self.otro = Otro
        self.bloque = Bloque
        self.valor_regresa = ValorRegresa
        self.llamada_funcion = LlamadaFunc

class SentenciaBloque(Sentencia):
    def __init__(self,Sentencia,Bloque):
        self.sentencia = Sentencia
        self.bloque = Bloque

class Otro(SentenciaBloque):
    def __init__(self, SentenciaBloque):
        self.vacio = None
        self.sentencia_bloque = SentenciaBloque

class Sentencias(Sentencia):
    def __init__(self,Sentencia,Sentencias):
        self.vacio = None
        self.sentencia = Sentencia
        self.sentencias = Sentencias

class Bloque(Sentencias):
    def __init__(self,Sentencias):
        self.sentencias = Sentencias

class ListaVar():
    def __init__(self,indetificador,ListaVar):
        self.vacio = None
        self.identificador = identificador
        self.ListaVar = ListaVar

class DefVar(ListaVar):
    def __init__(self,tipo, identificador,ListaVar):
        self.tipo = tipo
        self.identificador = identificador
        self.lista_variables = ListaVar

class DefLocal(DefVar,Sentencia):
    def __init__(self,DefVar,Sentencia):
        self.def_variables = DefVar
        self.sentencia = Sentencia

class DefLocales(DefLocal):
    def __init__(self,DefLocal, DefLocales):
        self.vacio = None
        self.def_local = DefLocal
        self.def_locales = DefLocales

class BloqueFuncion(DefLocales):
    def __init__(self,DefLocales):
        self.def_locales = DefLocales

class ListaParam():
    def __init__(self,tipo,identificador,ListaParam):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class Parametros(ListaParam):
    def __init__(self,ListaParam,tipo,identificador):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class DefFun(Parametros,BloqueFuncion):
    def __init__(self,Parametros,BloqueFuncion,tipo,identificador):
        self.parametros = Parametros
        self.bloque_funcion = BloqueFuncion
        self.tipo = tipo
        self.identificador = identificador

class Definicion(DefFun,DefVar):
    def __init__(self,DefVar,DefFun):
        self.def_variable = DefVar
        self.def_funcion = DefFun

class Definiciones(Definicion):
    def __init__(self,Definicion,Definiciones):
        self.vacio = None
        self.definicion = Definicion
        self.definiciones = Definiciones

class Programa(Definiciones):
    def __init__(self, Definiciones):
        self.definiciones = Definiciones



class Arbol():
    def __init__(self):
        self.lista_arbol = []
        self.lista_arbol_nombres = []
        self.regla = 0
        self.tipo = ""
        self.id = ""

    def tope_pila_arbol(self):
        return self.lista_arbol[len(self.lista_arbol)-1]
    def push_pila_arbol(self,elemento):
        self.lista_arbol.append(elemento)
    def pop_pila_arbol(self):
        return self.lista_arbol.pop()

    def forma_arbol(self,pila,pila_codigo,elementos,accion):
        self.regla = int(accion)-1
        self.tipo = ""
        self.id = ""

        if self.regla == PROGRAMA:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Programa(self.pop_pila_arbol()))

        elif self.regla == DEFINICIONES or self.regla == DEFINICIONES_V:
            if self.regla == DEFINICIONES_V:
                self.push_pila_arbol(Definiciones(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    pila.pop()
                    pila_codigo.pop()
                definicion = self.pop_pila_arbol()
                definiciones = self.pop_pila_arbol()
                self.push_pila_arbol(Definiciones(definicion,definiciones))

        elif self.regla == DEFINICION_FUN or self.regla == DEFINICION_VAR:
            if self.regla == DEFINICION_FUN:
                for i in range(elementos[self.regla]*2):
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(Definicion(None,self.pop_pila_arbol()))

        elif self.regla == DEFFUN:
            for i in range(elementos[self.regla]*2):
                if i == 9:
                    self.id = pila_codigo.top()
                if i == 11:
                    self.tipo = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            bloque_fun = self.pop_pila_arbol()
            param = self.pop_pila_arbol()
            self.push_pila_arbol(DefFun(param,bloque_fun,self.tipo,self.id))

        elif self.regla == BLOQFUNC:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    def_locales = self.tope_pila_arbol()
                    self.pop_pila_arbol()
                    self.push_pila_arbol(BloqueFuncion(def_locales))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCALES_V or self.regla == DEFLOCALES:
            if self.regla == DEFLOCALES_V:
                self.push_pila_arbol(DefLocales(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    pila.pop()
                    pila_codigo.pop()

        elif self.regla == PARAMETROS or self.regla == PARAMETROS_V:
            if self.regla == PARAMETROS_V:
                self.push_pila_arbol(Parametros(None,None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    #Falta la lista de parametros
                    pila.pop()
                    pila_codigo.pop()
        else:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
