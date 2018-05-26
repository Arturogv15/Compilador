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


class Node():
    def __init__():
        self.izquierda = None
        self.derecha = None
        self.centro = None

class Expresion_doble(Node):
    def __init__(self,Expresion1,Expresion2):
        self.expresion1 = Expresion1
        self.expresion2 = Expresion2

class Expresion(Node):
    def __init__(self,Expresion):
        self.expresion = Expresion

class Expresion_Termino(Node):
    def __init__(self, Termino):
        self.termino = Termino

class Termino_id(Node):
    def __init__(self,id):
        self.elemento = id

class Termino_real(Node):
    def __init__(self,real):
        self.elemento = real

class Termino_cadena(Node):
    def __init__(self,cadena):
        self.elemento = cadena

class Termino_entero(Node):
    def __init__(self,entero):
        self.elemento = entero

class Termino_llamada_funcion(Node):
    def __init__(self,LlamadaFuncion):
        self.llamada_funcion = LlamadaFuncion

class LlamadaFuncion(Node):
    def __init__(self,identificador,Argumentos):
        self.identificador = identificador
        self.argumentos = Argumentos

class ValorRegresa(Node):
    def __init__(self,Expresion):
        self.vacio = None
        self.expresion = Expresion

class ListaArgumentos(Node):
    def __init__(self,Expresion,ListaArgumentos):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos

class Argumentos(Node):
    def __init__(self,ListaArgumentos,Expresion):
        self.vacio = None
        self.expresion = Expresion
        self.lista_argumentos = ListaArgumentos


class Sentencia_asignacion(Node):
    def __init__(self,id,Expresion):
        self.expresion = Expresion
        self.identificador = id

class Sentencia_if(Node):
    def __init__(self,Expresion,SentenciaBloque,Otro):
        self.expresion = Expresion
        self.sentencia_bloque = SentenciaBloque
        self.otro = Otro

class Sentencia_while(Node):
    def __init__(self,Expresion,Bloque):
        self.expresion = Expresion
        self.bloque = Bloque

class Sentencia_return(Node):
    def __init__(self,ValorRegresa):
        self.valor_regresa = ValorRegresa

class Sentencia_llamada(Node):
    def __init__(self,LlamadaFuncion):
        self.llamada_funcion = LlamadaFuncion

class Bloque(Node):
    def __init__(self,Sentencias):
        self.sentencias = Sentencias

class Sentencias(Node):
    def __init__(self,Sentencia,Sentencias):
        self.vacio = None
        self.sentencia = Sentencia
        self.sentencias = Sentencias

class SentenciaBloque_B(Node):
    def __init__(self,Bloque):
        self.bloque = Bloque

class SentenciaBloque_S(Node):
    def __init__(self,Sentencia):
        self.sentencia = Sentencia

class Otro(Node):
    def __init__(self, SentenciaBloque):
        self.vacio = None
        self.sentencia_bloque = SentenciaBloque

class DefLocal_S(Node):
    def __init__(self,Sentencia):
        self.sentencia = Sentencia

class DefLocal_V(Node):
    def __init__(self,DefVar):
        self.def_variables = DefVar

class DefLocales(Node):
    def __init__(self,DefLocal, DefLocales):
        self.vacio = None
        self.def_local = DefLocal
        self.def_locales = DefLocales

class BloqueFuncion(Node):
    def __init__(self,DefLocales):
        self.def_locales = DefLocales

class DefFun(Node):
    def __init__(self,Parametros,BloqueFuncion,tipo,identificador):
        self.parametros = Parametros
        self.bloque_funcion = BloqueFuncion
        self.tipo = tipo
        self.identificador = identificador

class DefVar(Node):
    def __init__(self,tipo, identificador,ListaVar):
        self.tipo = tipo
        self.identificador = identificador
        self.lista_variables = ListaVar

class ListaVar(Node):
    def __init__(self,indetificador,ListaVar):
        self.vacio = None
        self.identificador = identificador
        self.ListaVar = ListaVar

class Parametros(Node):
    def __init__(self,ListaParam,tipo,identificador):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class ListaParam(Node):
    def __init__(self,tipo,identificador,ListaParam):
        self.vacio = None
        self.tipo = tipo
        self.identificador = identificador
        self.lista_parametros = ListaParam

class Definicion_Fun(Node):
    def __init__(self,DefFun):
        self.def_funcion = DefFun

class Definicion_Var(Node):
    def __init__(self,DefVar):
        self.def_variable = DefVar

class Definiciones(Node):
    def __init__(self,Definicion,Definiciones):
        self.vacio = None
        self.definicion = Definicion
        self.definiciones = Definiciones

class Programa(Node):
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

    def postorden(self,arbol):
        if arbol != None:
            self.postorden(arbol.izquierda)
            self.postorden(arbol.derecha)
            print(arbol.__dict__)
            #print("Raiz:   " + str(arbol))
            #print("Izq:    " + str(arbol.izquierda))
            #print("Der:    " + str(arbol.derecha))
            print("\n")

    def forma_arbol(self,pila,pila_codigo,elementos,accion):
        self.regla = int(accion)-1

        if self.regla == PROGRAMA:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            pop_pila = self.pop_pila_arbol()
            _Programa = Programa(pop_pila)
            _Programa.derecha = pop_pila
            _Programa.izquierda = None
            self.push_pila_arbol(_Programa)

        elif self.regla == DEFINICIONES or self.regla == DEFINICIONES_V:
            if self.regla == DEFINICIONES_V:
                _Definiciones = Definiciones(None,None)
                _Definiciones.izquierda = None
                _Definiciones.derecha = None
                self.push_pila_arbol(_Definiciones)
            else:
                for i in range(elementos[self.regla]*2):
                    pila.pop()
                    pila_codigo.pop()
                definiciones = self.pop_pila_arbol()
                definicion = self.pop_pila_arbol()
                _Definiciones = Definiciones(definicion,definiciones)
                _Definiciones.izquierda = definicion
                _Definiciones.derecha = definiciones
                self.push_pila_arbol(_Definiciones)

        elif self.regla == DEFINICION_FUN:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            pop_pila = self.pop_pila_arbol()
            _definicion = Definicion_Fun(pop_pila)
            _definicion.derecha = pop_pila
            _definicion.izquierda = None
            self.push_pila_arbol(_definicion)

        elif self.regla == DEFINICION_VAR:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
            pop_pila = self.pop_pila_arbol()
            _definicion = Definicion_Var(pop_pila)
            _definicion.izquierda = pop_pila
            _definicion.derecha = None
            self.push_pila_arbol(_definicion)

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
            def_fun = DefFun(param,bloque_fun,self.tipo,self.id)
            def_fun.izquierda = param
            def_fun.derecha = bloque_fun
            self.push_pila_arbol(def_fun)

        elif self.regla == BLOQFUNC:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                     def_locales = self.pop_pila_arbol()
                     bloque_fun = BloqueFuncion(def_locales)
                     bloque_fun.derecha = def_locales
                     bloque_fun.izquierda = None
                     self.push_pila_arbol(bloque_fun)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCALES_V or self.regla == DEFLOCALES:
            if self.regla == DEFLOCALES_V:
                def_locales = DefLocales(None,None)
                def_locales.derecha = None
                def_locales.izquierda = None
                self.push_pila_arbol(def_locales)
            else:
                for i in range(elementos[self.regla]*2):
                    if i==1:
                        self.def_locales = self.pop_pila_arbol()
                    elif i==3:
                        self.def_local = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                def_locales = DefLocales(self.def_local,self.def_locales)
                def_locales.derecha = self.def_locales
                def_locales.izquierda = self.def_local
                self.push_pila_arbol(def_locales)

        elif self.regla == PARAMETROS or self.regla == PARAMETROS_V:
            if self.regla == PARAMETROS_V:
                _parametros = Parametros(None,None,None)
                _parametros.derecha = None
                _parametros.izquierda = None
                self.push_pila_arbol(_parametros)
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
                _parametros = Parametros(self.lista_parametros,self.tipo,self.id)
                _parametros.derecha = self.lista_parametros
                _parametros.izquierda = None
                self.push_pila_arbol(_parametros)

        elif self.regla == LISTAPARAM or self.regla == LISTAPARAM_V:
            if self.regla == LISTAPARAM_V:
                _lista_param = ListaParam(None,None,None)
                _lista_param.derecha = None
                _lista_param.izquierda = None
                self.push_pila_arbol(_lista_param)
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
                _lista_param = ListaParam(self.tipo,self.id,self.lista_parametros)
                if _lista_param == None:
                    _lista_param.derecha = None
                else:
                    _lista_param.derecha = self.lista_parametros
                _lista_param.izquierda = None
                self.push_pila_arbol(_lista_param)

        elif self.regla == LLAMADAFUN:
            for i in range(elementos[self.regla]*2):
                if i==3:
                    self.argumentos = self.pop_pila_arbol()
                elif i == 7:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            _llamada_fun = LlamadaFuncion(self.id,self.argumentos)
            _llamada_fun.derecha = self.argumentos
            _llamada_fun.izquierda = None
            self.push_pila_arbol(_llamada_fun)

        elif self.regla == TERMINO_CALLFUN:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    llamada_funcion = self.pop_pila_arbol()
                    ter_llamada = Termino_llamada_funcion(llamada_funcion)
                    ter_llamada.derecha = llamada_funcion
                    ter_llamada.izquierda = None
                    self.push_pila_arbol(ter_llamada)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_ID:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            termino_id = Termino_id(self.id)
            termino_id.derecha = None
            termino_id.izquierda = None
            self.push_pila_arbol(termino_id)

        elif self.regla == TERMINO_INT:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    entero = pila_codigo.top()
                    termino_entero = Termino_entero(entero)
                    termino_entero.derecha = None
                    termino_entero.izquierda = None
                    self.push_pila_arbol(termino_entero)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_CAD:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    cadena = pila_codigo.top()
                    termino_cadena = Termino_cadena(cadena)
                    termino_cadena.derecha = None
                    termino_cadena.izquierda = None
                    self.push_pila_arbol(termino_cadena)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == TERMINO_REAL:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    real = pila_codigo.top()
                    termino_real = Termino_real(real)
                    termino_real.izquierda = None
                    termino_real.derecha = None
                    self.push_pila_arbol(termino_real)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION:
            for i in range(elementos[self.regla]*2):
                if i==3:
                    expresion = self.pop_pila_arbol()
                    _expresion = Expresion(expresion)
                    _expresion.izquierda = None
                    _expresion.derecha = expresion
                    self.push_pila_arbol(_expresion)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION_TERMINO:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    termino = self.pop_pila_arbol()
                    exp_termino = Expresion_Termino(termino)
                    exp_termino.derecha = termino
                    exp_termino.izquierda = None
                    self.push_pila_arbol(exp_termino)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == EXPRESION_MAS or self.regla == EXPRESION_NOT:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    expresion = self.pop_pila_arbol()
                    exp_mas_not = Expresion(expresion)
                    exp_mas_not.derecha = expresion
                    exp_mas_not.izquierda = None
                    self.push_pila_arbol(exp_mas_not)
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
            exp_doble = Expresion_doble(self.expresion1,self.expresion2)
            exp_doble.derecha = self.expresion2
            exp_doble.izquierda = self.expresion1
            self.push_pila_arbol(exp_doble)

        elif self.regla == EXPRESION_MULT or self.regla == EXPRESION_AND or self.regla == EXPRESION_OR:
            for i in range(elementos[self.regla]*2):
                if i==1:
                    self.expresion2 = self.pop_pila_arbol()
                elif i==5:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            exp_doble = Expresion_doble(self.expresion1,self.expresion2)
            exp_doble.derecha = self.expresion2
            exp_doble.izquierda = self.expresion1
            self.push_pila_arbol(exp_doble)

        elif self.regla == SENTENCIA_ASIG:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    self.expresion1 = self.pop_pila_arbol()
                elif i == 7:
                    self.id = pila_codigo.top()
                pila.pop()
                pila_codigo.pop()
            sent_asig = Sentencia_asignacion(self.id,self.expresion1)
            sent_asig.derecha = self.expresion1
            sent_asig.izquierda = None
            self.push_pila_arbol(sent_asig)

        elif self.regla == SENTENCIAS or self.regla == SENTENCIAS_V:
            if self.regla == SENTENCIAS_V:
                sentencias = Sentencias(None,None)
                sentencias.derecha = None
                sentencias.izquierda = None
                self.push_pila_arbol(sentencias)
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.sentencias = self.pop_pila_arbol()
                    elif i == 3:
                        self.sentencia = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                sentencias = Sentencias(self.sentencia,self.sentencias)
                sentencias.derecha = self.sentencias
                sentencias.izquierda = self.sentencia
                self.push_pila_arbol(sentencias)

        elif self.regla == BLOQUE:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    self.sentencias = self.pop_pila_arbol()
                    bloque = Bloque(self.sentencias)
                    bloque.derecha = self.sentencias
                    bloque.izquierda = None
                    self.push_pila_arbol(bloque)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == SENTENCIABLOQUE_BLOQ:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    bloque = self.pop_pila_arbol()
                    sent_bloque_b = SentenciaBloque_B(bloque)
                    sent_bloque_b.derecha = bloque
                    sent_bloque_b.izquierda = None
                    self.push_pila_arbol(sent_bloque_b)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == SENTENCIABLOQUE_SENT:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    sentencia = self.pop_pila_arbol()
                    sent_bloque_s = SentenciaBloque_S(sentencia)
                    sent_bloque_s.derecha = sentencia
                    sent_bloque_s.izquierda = None
                    self.push_pila_arbol(sent_bloque_s)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == OTRO or self.regla == OTRO_V:
            if self.regla == OTRO_V:
                otro = Otro(None)
                otro.derecha = None
                otro.izquierda = None
                self.push_pila_arbol(otro)
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        sentencia_bloque = self.pop_pila_arbol()
                        otro = Otro(sentencia_bloque)
                        otro.derecha = sentencia_bloque
                        otro.izquierda = None
                        self.push_pila_arbol(otro)
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
            _if = Sentencia_if(self.expresion1,self.sentencia_bloque,self.otro)
            _if.derecha = self.otro
            _if.izquierda = self.expresion1
            _if.centro = self.sentencia_bloque
            self.push_pila_arbol(_if)

        elif self.regla == SENTENCIA_WHILE:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.bloque = self.pop_pila_arbol()
                elif i == 5:
                    self.expresion1 = self.pop_pila_arbol()
                pila.pop()
                pila_codigo.pop()
            _while = Sentencia_while(self.expresion1,self.bloque)
            _while.izquierda = self.expresion1
            _while.derecha = self.bloque
            self.push_pila_arbol(_while)

        elif self.regla == SENTENCIA_RETURN:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    valor_regresa = self.pop_pila_arbol()
                    _return = Sentencia_return(valor_regresa)
                    _return.izquierda = None
                    _return.derecha = valor_regresa
                    self.push_pila_arbol(_return)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == SENTENCIA_CALLFUN:
            for i in range(elementos[self.regla]*2):
                if i == 3:
                    llamada_funcion = self.pop_pila_arbol()
                    _llamada = Sentencia_llamada(llamada_funcion)
                    _llamada.izquierda = None
                    _llamada.derecha = llamada_funcion
                    self.push_pila_arbol(_llamada)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCAL_SENT:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.sentencia = self.pop_pila_arbol()
                    defloc = DefLocal_S(self.sentencia)
                    defloc.derecha = self.sentencia
                    defloc.izquierda = None
                    self.push_pila_arbol(defloc)
                pila.pop()
                pila_codigo.pop()

        elif self.regla == DEFLOCAL_VAR:
            for i in range(elementos[self.regla]*2):
                if i == 1:
                    self.variable = self.pop_pila_arbol()
                    defloc = DefLocal_V(self.variable)
                    defloc.derecha = self.sentencia
                    defloc.izquierda = None
                    self.push_pila_arbol(defloc)
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
            def_var = DefVar(self.tipo,self.id,self.lista_variables)
            def_var.derecha = self.lista_variables
            def_var.izquierda = None
            self.push_pila_arbol(def_var)

        elif self.regla == LISTAVAR or self.regla == LISTAVAR_V:
            if self.regla == LISTAVAR_V:
                lista_var = ListaVar(None,None)
                lista_var.derecha = None
                lista_var.izquierda = None
                self.push_pila_arbol(lista_var)
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.lista_variables = self.pop_pila_arbol()
                    elif i == 3:
                        self.id = pila_codigo.top()
                    pila.pop()
                    pila_codigo.pop()
                lista_var = ListaVar(self.id,self.lista_variables)
                lista_var.derecha = self.lista_variables
                lista_var.izquierda = None
                self.push_pila_arbol(lista_var)


        elif self.regla == VALORREGRESA or self.regla == VALORREGRESA_V:
            if self.regla == VALORREGRESA_V:
                valor_r = ValorRegresa(None)
                valor_r.derecha = None
                valor_r.izquierda = None
                self.push_pila_arbol(valor_r)
            else:
                for i in range(elementos[self.regla]*2):
                    if i == 1:
                        self.expresion1 = self.pop_pila_arbol()
                        valor_r = ValorRegresa(self.expresion1)
                        valor_r.derecha = self.expresion1
                        valor_r.izquierda = None
                        self.push_pila_arbol(valor_r)
                    pila.pop()
                    pila_codigo.pop()

        elif self.regla == ARGUMENTOS or self.regla == ARGUMENTOS_V:
            if self.regla == ARGUMENTOS_V:
                args = Argumentos(None,None)
                args.derecha = None
                args.izquierda = None
                self.push_pila_arbol(args)
            else:
                for i in range(elementos[self.regla]*2):
                    if  i == 1:
                        self.lista_argumentos = self.pop_pila_arbol()
                    elif i == 3:
                        self.expresion1 = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                args = Argumentos(self.lista_argumentos,self.expresion1)
                args.derecha = self.lista_argumentos
                args.izquierda = self.expresion1
                self.push_pila_arbol(args)

        elif self.regla == LISTAARGUMENTOS or self.regla == LISTAARGUMENTOS_V:
            if self.regla == LISTAARGUMENTOS_V:
                list_args = ListaArgumentos(None,None)
                list_args.derecha = None
                list_args.izquierda = None
                self.push_pila_arbol(list_args)
            else:
                for i in range(elementos[self.regla]*2):
                    if  i == 1:
                        self.lista_argumentos = self.pop_pila_arbol()
                    elif i == 3:
                        self.expresion1 = self.pop_pila_arbol()
                    pila.pop()
                    pila_codigo.pop()
                list_args = ListaArgumentos(self.expresion1,self.lista_argumentos)
                list_args.derecha = self.lista_argumentos
                list_args.izquierda = self.expresion1
                self.push_pila_arbol(list_args)

        else:
            for i in range(elementos[self.regla]*2):
                pila.pop()
                pila_codigo.pop()
