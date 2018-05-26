
FUNCION = 1
PARAMETRO = 2
VARIABLE = 3


class Semantico:
    def __init__(self):
        self.tabla_simbolos = []
        self.nombre = None
        self.tipo = None
        self.tipo_dato = None
        self.funcion = None

    def busca_simbolo(self,simbolo,tipodato,tipo,funcion=None):

        if len(self.tabla_simbolos) == 0:
            return False
        else:
            if tipo == FUNCION:
                for i in range(len(self.tabla_simbolos)):
                    if self.tabla_simbolos[i].tipo == 'funcion':
                        if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].tipo_dato == tipodato:
                            return True
                return False
            elif tipo == PARAMETRO:
                    for i in range(len(self.tabla_simbolos)):
                        if self.tabla_simbolos[i].tipo == 'parametro' and self.tabla_simbolos[i].funcion == funcion:
                            if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].tipo_dato == tipodato:
                                return True
                    return False
            elif tipo == VARIABLE:
                return False


    def analiza(self,elemento,arbol):
        obj = Semantico()

        if elemento == 'Programa':
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False
            #print(arbol.__dict__)

        elif elemento == 'Definiciones':
            if arbol.izquierda == None or arbol.derecha == None:       #Si las definiciones son vacias
                arbol.valido = True
            elif arbol.derecha == None:               #Si una definicion es vacia
                if arbol.izquierda.valido == True:
                    arbol.valido = True
            else:                                  #Si la izquierda y derecha no son vacias
                if arbol.izquierda.valido == True and arbol.derecha.valido == True:
                    arbol.valido = True
                else:
                    arbol.valido = False

        elif elemento == 'Definicion_Fun':
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'DefFun':
            #print(arbol.__dict__)
            id = arbol.identificador
            tipo = arbol.tipo
            if self.busca_simbolo(id,tipo,FUNCION) == False:
                arbol.valido = True
                obj.tipo = 'funcion'
                obj.nombre = id
                obj.tipo_dato = tipo
                self.tabla_simbolos.append(obj)
            else:
                arbol.valido = False

        elif elemento == 'Parametros':
            print(arbol.__dict__)
            id = arbol.identificador
            tipo = arbol.tipo
            funcion = arbol.funcion
            if self.busca_simbolo(id,tipo,PARAMETRO,funcion) == False:
                obj.tipo = 'parametro'
                obj.nombre = id
                obj.tipo_dato = tipo
                obj.funcion = funcion
                arbol.valido = True
                self.tabla_simbolos.append(obj)
            else:
                arbol.valido = False







#
