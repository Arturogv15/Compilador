PROGRAMA = 0                                #
DEFINICIONES_V = 1                          #
DEFINICIONES = 2                            #
DEFINICION_VAR = 3                          #
DEFINICION_FUN = 4                          #
DEFVAR = 5                                  #
LISTAVAR_V = 6                              #
LISTAVAR = 7                                #
DEFFUN = 8                                  #
PARAMETROS_V = 9                            #
PARAMETROS = 10                             #
LISTAPARAM_V = 11                           #
LISTAPARAM = 12                             #
BLOQFUNC = 13                               #
DEFLOCALES_V = 14                           #
DEFLOCALES = 15                             #
DEFLOCAL_VAR = 16                           #
DEFLOCAL_SENT = 17                          #
SENTENCIAS_V = 18                           #
SENTENCIAS = 19                             #
SENTENCIA_ASIG = 20                         #
SENTENCIA_IF = 21                           #
SENTENCIA_WHILE = 22                        #
SENTENCIA_RETURN = 23                       #
SENTENCIA_CALLFUN = 24                      #
OTRO_V = 25                                 #
OTRO = 26                                   #
BLOQUE = 27                                 #
VALORREGRESA_V = 28                         #
VALORREGRESA = 29                           #
ARGUMENTOS_V = 30                           #
ARGUMENTOS = 31                             #
LISTAARGUMENTOS_V = 32                      #
LISTAARGUMENTOS = 33                        #
TERMINO_CALLFUN = 34
TERMINO_ID = 35                             #
TERMINO_INT = 36                            #
TERMINO_REAL = 37                           #
TERMINO_CAD = 38                            #
LLAMADAFUN = 39
SENTENCIABLOQUE_SENT = 40                   #
SENTENCIABLOQUE_BLOQ = 41                   #
EXPRESION = 42                              #
EXPRESION_MAS = 43                          #
EXPRESION_NOT = 44                          #
EXPRESION_PLUS = 45                         #
EXPRESION_MULT = 46                         #
EXPRESION_REL = 47                          #
EXPRESION_IGUAL = 48                        #
EXPRESION_AND = 49                          #
EXPRESION_OR = 50                           #
EXPRESION_TERMINO = 51                      #

class Expresion_doble():
    def __init__(self,Expresion1,Expresion2):
        self.expresion1 = Expresion1
        self.expresion2 = Expresion2

class Expresion():
    def __init__(self,Expresion):
        self.expresion = Expresion

class Expresion_Termino():
    def __init__(self, Termino):
        self.termino = Termino

class Termino_id():
    def __init__(self,id):
        self.elemento = id

class Termino_real():
    def __init__(self,real):
        self.elemento = real

class Termino_cadena():
    def __init__(self,cadena):
        self.elemento = cadena

class Termino_entero():
    def __init__(self,entero):
        self.elemento = entero

class Termino_llamada_funcion():
    def __init__(self,LlamadaFuncion):
        self.llamada_funcion = LlamadaFuncion

class LlamadaFuncion():
    def __init__(self,identificador,Argumentos):
        self.identificador = identificador
        self.argumentos = Argumentos

class ValorRegresa():
    def __init__(self,Expresion):
        self.vacio = None
        self.expresion = Expresion

class ListaArgumentos():
    def __init__(self,Expresion,ListaArgumentos):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos

class Argumentos():
    def __init__(self,ListaArgumentos,Expresion):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos


class Sentencia_asignacion():
    def __init__(self,id,Expresion):
        self.expresion = Expresion
        self.identificador = id

class Sentencia_if():
    def __init__(self,Expresion,SentenciaBloque,Otro):
        self.expresion = Expresion
        self.sentencia_bloque = SentenciaBloque
        self.otro = Otro

class Sentencia_while():
    def __init__(self,Expresion,Bloque):
        self.expresion = Expresion
        self.bloque = Bloque

class Sentencia_return():
    def __init__(self,ValorRegresa):
        self.valor_regresa = ValorRegresa

class Sentencia_llamada():
    def __init__(self,LlamadaFuncion):
        self.llamada_funcion = LlamadaFuncion

class Bloque():
    def __init__(self,Sentencias):
        self.sentencias = Sentencias

class Sentencias():
    def __init__(self,Sentencia,Sentencias):
        self.vacio = None
        self.sentencia = Sentencia
        self.sentencias = Sentencias

class SentenciaBloque_B():
    def __init__(self,Bloque):
        self.bloque = Bloque

class SentenciaBloque_S():
    def __init__(self,Sentencia):
        self.sentencia = Sentencia

class Otro():
    def __init__(self, SentenciaBloque):
        self.vacio = None
        self.sentencia_bloque = SentenciaBloque

class DefLocal_S():
    def __init__(self,Sentencia):
        self.sentencia = Sentencia

class DefLocal_V():
    def __init__(self,DefVar):
        self.def_variables = DefVar

class DefLocales():
    def __init__(self,DefLocal, DefLocales):
        self.vacio = None
        self.def_local = DefLocal
        self.def_locales = DefLocales

class BloqueFuncion():
    def __init__(self,DefLocales):
        self.def_locales = DefLocales

class DefFun():
    def __init__(self,Parametros,BloqueFuncion,tipo,identificador):
        self.parametros = Parametros
        self.bloque_funcion = BloqueFuncion
        self.tipo = tipo
        self.identificador = identificador

class DefVar():
    def __init__(self,tipo, identificador,ListaVar):
        self.tipo = tipo
        self.identificador = identificador
        self.lista_variables = ListaVar

class ListaVar():
    def __init__(self,indetificador,ListaVar):
        self.vacio = None
        self.identificador = identificador
        self.ListaVar = ListaVar

class Parametros():
    def __init__(self,ListaParam,tipo,identificador):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class ListaParam():
    def __init__(self,tipo,identificador,ListaParam):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class Definicion_Fun():
    def __init__(self,DefFun):
        self.def_funcion = DefFun

class Definicion_Var():
    def __init__(self,DefVar):
        self.def_variable = DefVar

class Definiciones():
    def __init__(self,Definicion,Definiciones):
        self.vacio = None
        self.definicion = Definicion
        self.definiciones = Definiciones

class Programa():
    def __init__(self, Definiciones):
        self.definiciones = Definiciones



class Arbol():
    def __init__(self):
        self.lista_arbol = []
        self.lista_arbol_nombres = []
        self.regla = 0
        self.tipo = ""
        self.id = ""
        self.expresion1 = ""
        self.expresion2 = ""
        self.sentencia = ""
        self.sentencias = ""
        self.otro = ""
        self.bloque = ""
        self.sentencia_bloque = ""
        self.def_local = ""
        self.def_locales = ""
        self.lista_variables = ""
        self.lista_parametros = ""
        self.lista_argumentos = ""
        self.variable = ""
        self.argumentos = ""

    def push_pila_arbol(self,elemento):
        self.lista_arbol.append(elemento)
    def pop_pila_arbol(self):
        return self.lista_arbol.pop()

    def forma_arbol(self,pila,pila_codigo,elementos,accion):
        self.regla = int(accion)-1

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
                definiciones = self.pop_pila_arbol()
                definicion = self.pop_pila_arbol()
                self.push_pila_arbol(Definiciones(definicion,definiciones))

        elif self.regla == DEFINICION_FUN:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Definicion_Fun(self.pop_pila_arbol()))

        elif self.regla == DEFINICION_VAR:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Definicion_Var(self.pop_pila_arbol()))

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
                    def_locales = self.pop_pila_arbol()
                    self.push_pila_arbol(BloqueFuncion(def_locales))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCALES_V or self.regla == DEFLOCALES:
            if self.regla == DEFLOCALES_V:
                self.push_pila_arbol(DefLocales(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i==1:
                        self.def_locales = self.pop_pila_arbol()
                    elif i==3:
                        self.def_local = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(DefLocales(self.def_local,self.def_locales))

        elif self.regla == PARAMETROS or self.regla == PARAMETROS_V:
            if self.regla == PARAMETROS_V:
                self.push_pila_arbol(Parametros(None,None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.lista_parametros = self.pop_pila_arbol()
                    elif i == 3:
                        self.id = pila_codigo.top()
                    elif i == 5:
                        self.tipo = pila_codigo.top()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(Parametros(self.lista_parametros,self.tipo,self.id))

        elif self.regla == LISTAPARAM or self.regla == LISTAPARAM_V:
            if self.regla == LISTAPARAM_V:
                self.push_pila_arbol(ListaParam(None,None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.lista_parametros = self.pop_pila_arbol()
                    elif i == 3:
                        self.id = pila_codigo.top()
                    elif i == 5:
                        self.tipo = pila_codigo.top()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(ListaParam(self.tipo,self.id,self.lista_parametros))

        elif self.regla == LLAMADAFUN:
            for i in range(elementos[self.regla]*2):
                if i==3:
                    self.argumentos = self.pop_pila_arbol()
                elif i == 7:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(LlamadaFuncion(self.id,self.argumentos))

        elif self.regla == TERMINO_CALLFUN:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    llamada_funcion = self.pop_pila_arbol()
                    self.push_pila_arbol(Termino_llamada_funcion(llamada_funcion))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_ID:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Termino_id(self.id))

        elif self.regla == TERMINO_INT:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    entero = pila_codigo.top()
                    self.push_pila_arbol(Termino_entero(entero))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_CAD:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    cadena = pila_codigo.top()
                    self.push_pila_arbol(Termino_cadena(cadena))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_REAL:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    real = pila_codigo.top()
                    self.push_pila_arbol(Termino_real(real))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION:
            for i in range(elementos[self.regla]*2):
                if i==3:
                    expresion = self.pop_pila_arbol()
                    self.push_pila_arbol(Expresion(expresion))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION_TERMINO:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    termino = self.pop_pila_arbol()
                    self.push_pila_arbol(Expresion_Termino(termino))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION_MAS or self.regla == EXPRESION_NOT:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    expresion = self.pop_pila_arbol()
                    self.push_pila_arbol(Expresion(expresion))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION_IGUAL or self.regla == EXPRESION_REL or self.regla == EXPRESION_PLUS:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    self.expresion2 = self.pop_pila_arbol()
                elif i==5:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Expresion_doble(self.expresion1,self.expresion2))

        elif self.regla == EXPRESION_MULT or self.regla == EXPRESION_AND or self.regla == EXPRESION_OR:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    self.expresion2 = self.pop_pila_arbol()
                elif i==5:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Expresion_doble(self.expresion1,self.expresion2))

        elif self.regla == SENTENCIA_ASIG:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    self.expresion1 = self.pop_pila_arbol()
                elif i == 7:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Sentencia_asignacion(self.id,self.expresion1))

        elif self.regla == SENTENCIAS or self.regla == SENTENCIAS_V:
            if self.regla == SENTENCIAS_V:
                self.push_pila_arbol(Sentencias(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.sentencias = self.pop_pila_arbol()
                    elif i == 3:
                        self.sentencia = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(Sentencias(self.sentencia,self.sentencias))

        elif self.regla == BLOQUE:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    self.sentencias = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Bloque(self.sentencias))

        elif self.regla == SENTENCIABLOQUE_BLOQ:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    bloque = self.pop_pila_arbol()
                    self.push_pila_arbol(SentenciaBloque_B(bloque))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == SENTENCIABLOQUE_SENT:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    sentencia = self.pop_pila_arbol()
                    self.push_pila_arbol(SentenciaBloque_S(sentencia))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == OTRO or self.regla == OTRO_V:
            if self.regla == OTRO_V:
                self.push_pila_arbol(Otro(None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        sentencia_bloque = self.pop_pila_arbol()
                        self.push_pila_arbol(Otro(sentencia_bloque))
                    pila.pop()
                    pila_codigo.pop()

        elif self.regla == SENTENCIA_IF:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.otro = self.pop_pila_arbol()
                elif i == 3:
                    self.sentencia_bloque = self.pop_pila_arbol()
                elif i == 7:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Sentencia_if(self.expresion1,self.sentencia_bloque,self.otro))

        elif self.regla == SENTENCIA_WHILE:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.bloque = self.pop_pila_arbol()
                elif i == 5:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(Sentencia_while(self.expresion1,self.bloque))

        elif self.regla == SENTENCIA_RETURN:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    valor_regresa = self.pop_pila_arbol()
                    self.push_pila_arbol(Sentencia_return(valor_regresa))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == SENTENCIA_CALLFUN:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    llamada_funcion = self.pop_pila_arbol()
                    self.push_pila_arbol(Sentencia_llamada(llamada_funcion))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCAL_SENT:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.sentencia = self.pop_pila_arbol()
                    self.push_pila_arbol(DefLocal_S(self.sentencia))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCAL_VAR:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.variable = self.pop_pila_arbol()
                    self.push_pila_arbol(DefLocal_V(self.variable))
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFVAR:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    self.lista_variables = self.pop_pila_arbol()
                elif i == 5:
                    self.id = pila_codigo.top()
                elif i == 7:
                    self.tipo = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            self.push_pila_arbol(DefVar(self.tipo,self.id,self.lista_variables))

        elif self.regla == LISTAVAR or self.regla == LISTAVAR_V:
            if self.regla == LISTAVAR_V:
                self.push_pila_arbol(ListaVar(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.lista_variables = self.pop_pila_arbol()
                    elif i == 3:
                        self.id = pila_codigo.top()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(ListaVar(self.id,self.lista_variables))


        elif self.regla == VALORREGRESA or self.regla == VALORREGRESA_V:
            if self.regla == VALORREGRESA_V:
                self.push_pila_arbol(ValorRegresa(None))
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.expresion1 = self.pop_pila_arbol()
                        self.push_pila_arbol(ValorRegresa(self.expresion1))
                    pila.pop()
                    pila_codigo.pop()

        elif self.regla == ARGUMENTOS or self.regla == ARGUMENTOS_V:
            if self.regla == ARGUMENTOS_V:
                self.push_pila_arbol(Argumentos(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if  i == 1:
                        self.lista_argumentos = self.pop_pila_arbol()
                    elif i == 3:
                        self.expresion1 = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(Argumentos(self.lista_argumentos,self.expresion1))

        elif self.regla == LISTAARGUMENTOS or self.regla == LISTAARGUMENTOS_V:
            if self.regla == LISTAARGUMENTOS_V:
                self.push_pila_arbol(ListaArgumentos(None,None))
            else:
                for i in range(elementos[self.regla]*2):
                    if  i == 1:
                        self.lista_argumentos = self.pop_pila_arbol()
                    elif i == 3:
                        self.expresion1 = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                self.push_pila_arbol(ListaArgumentos(self.expresion1,self.lista_argumentos))

        else:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
