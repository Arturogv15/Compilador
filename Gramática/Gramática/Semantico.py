
FUNCION = 1
PARAMETRO = 2
DEFINICIONVAR = 3
VARIABLE = 4
FUNCION_REGRESA = 5
LLAMADA_FUNCION = 6


class Semantico:
    def __init__(self):
        self.tabla_simbolos = []
        self.nombre = None
        self.tipo = None
        self.tipo_dato = None
        self.funcion = None
        self.bandera = False

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

            elif tipo == FUNCION_REGRESA:
                for i in range(len(self.tabla_simbolos)):
                        if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].tipo_dato == tipodato:
                            return True
                return False

            elif tipo == PARAMETRO:
                    for i in range(len(self.tabla_simbolos)):
                        if self.tabla_simbolos[i].tipo == 'parametro' and self.tabla_simbolos[i].funcion == funcion:
                            if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].tipo_dato == tipodato:
                                return True
                    return False

            elif tipo == DEFINICIONVAR:
                if funcion == None:
                    for i in range(len(self.tabla_simbolos)):
                        if self.tabla_simbolos[i].tipo == 'variable':
                            if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].tipo_dato == tipodato:
                                return True
                    return False
                else:
                    #print(funcion,tipodato,simbolo)
                    for i in range(len(self.tabla_simbolos)):
                        #print(self.tabla_simbolos[i].tipo, self.tabla_simbolos[i].funcion, self.tabla_simbolos[i].nombre)
                        if self.tabla_simbolos[i].tipo == 'variable' or self.tabla_simbolos[i].tipo == 'parametro':
                            if  self.tabla_simbolos[i].funcion == funcion and self.tabla_simbolos[i].nombre == simbolo:
                                print(self.tabla_simbolos[i].funcion,funcion)
                                print(self.tabla_simbolos[i].nombre,simbolo)
                                print(self.tabla_simbolos[i].tipo_dato,tipodato)
                                if self.tabla_simbolos[i].tipo_dato == tipodato:
                                    return True
                    return False

            elif tipo == VARIABLE:
                for i in range(len(self.tabla_simbolos)):
                    #print(self.tabla_simbolos[i].tipo, self.tabla_simbolos[i].funcion, self.tabla_simbolos[i].nombre)
                    if self.tabla_simbolos[i].tipo == 'variable' or self.tabla_simbolos[i].tipo == 'parametro':
                        if self.tabla_simbolos[i].nombre == simbolo and self.tabla_simbolos[i].funcion == funcion:
                            return {'band': True, 'tipo': self.tabla_simbolos[i].tipo_dato}
                return {'band': False}

            elif tipo == LLAMADA_FUNCION:
                for i in range(len(self.tabla_simbolos)):
                    if self.tabla_simbolos[i].tipo == 'funcion' and self.tabla_simbolos[i].nombre == simbolo:
                        print('hi')

    def analiza(self,elemento,arbol):

        if elemento == 'Programa':
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False
            #print(arbol.__dict__)

        elif elemento == 'Definiciones':
            #print(arbol.__dict__)
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

        elif elemento == 'Definicion_Var':
            #print(arbol.__dict__)
            if arbol.izquierda.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'DefVar':
            self.bandera = False
            print(arbol.__dict__)
            id = arbol.identificador
            tipo = arbol.tipo
            funcion = arbol.funcion
            if self.busca_simbolo(id,tipo,DEFINICIONVAR,funcion) == False:
                obj = Semantico()
                obj.tipo = 'variable'
                obj.tipo_dato = tipo
                obj.nombre = id
                self.tabla_simbolos.append(obj)
                arbol.valido = True
            else:
                arbol.valido = False

            nuevo_arbol = arbol
            while arbol.derecha != None:
                if arbol.derecha != None:
                    id = arbol.derecha.identificador
                    if self.busca_simbolo(id,tipo,DEFINICIONVAR,funcion) == False:
                        obj2 = Semantico()
                        obj2.tipo = 'variable'
                        obj2.tipo_dato = tipo
                        obj2.nombre = id
                        self.tabla_simbolos.append(obj2)
                        arbol.derecha.valido = True
                    else:
                        arbol.derecha.valido = False
                        self.bandera = True
                        break

                    if arbol.derecha.valido == True:
                        arbol = arbol.derecha
                        arbol.valido = True
                    else:
                        arbol = arbol.derecha
                        arbol.valido = False

            #print("BANDERA " + str(self.bandera))
            if self.bandera == True or nuevo_arbol.valido == False:
                return False
            else:
                return True

        elif elemento == 'DefFun':
            print(arbol.__dict__)
            obj = Semantico()
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

            print(arbol.valido)
            if arbol.izquierda.valido == True and arbol.valido == True and arbol.derecha.valido:
            #if arbol.izquierda.valido == True and arbol.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Parametros':
            #print(arbol.__dict__)
            self.bandera = False
            id = arbol.identificador
            tipo = arbol.tipo
            funcion = arbol.funcion
            if self.busca_simbolo(id,tipo,PARAMETRO,funcion) == False:
                obj = Semantico()
                obj.tipo = 'parametro'
                obj.nombre = id
                obj.tipo_dato = tipo
                obj.funcion = funcion
                arbol.valido = True
                if obj.nombre != None:
                    self.tabla_simbolos.append(obj)
            else:
                arbol.valido = False

            nuevo_arbol = arbol
            while(arbol.derecha != None):
                id = arbol.derecha.identificador
                tipo = arbol.derecha.tipo
                funcion = nuevo_arbol.funcion
                if self.busca_simbolo(id,tipo,PARAMETRO,funcion) == False:
                    obj2 = Semantico()
                    obj2.tipo = 'parametro'
                    obj2.nombre = id
                    obj2.tipo_dato = tipo
                    obj2.funcion = funcion
                    arbol.derecha.valido = True
                    if obj2.nombre != None:
                        self.tabla_simbolos.append(obj2)
                else:
                    arbol.derecha.valido = False
                    self.bandera = True
                    break

                if arbol.derecha.valido == True:
                    arbol = arbol.derecha
                    arbol.valido = True
                else:
                    arbol = arbol.derecha
                    arbol.valido = False

            print(self.bandera)
            if self.bandera == True or nuevo_arbol.valido == False:
                return False
            else:
                return True

        elif elemento == 'BloqueFuncion':
            print(arbol.__dict__)
            #arbol.valido = True
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'DefLocales':
            print(arbol.__dict__)
            arbol.valido = True
            if arbol.derecha == None and arbol.izquierda == None:    #Esta vacio el nodo
                arbol.valido = True
            elif arbol.derecha == None:             #No tiene deflocales
                if arbol.izquierda.valido == True:
                    arbol.valido = True
            else:
                #print(arbol.derecha.valido, arbol.izquierda.derecha.derecha.valido)                   #Tiene deflocal y deflocales
                if arbol.derecha.valido == True and arbol.izquierda.valido == True:
                    arbol.valido = True
                else:
                    arbol.valido = False

        elif elemento == 'DefLocal_V':
            self.bandera = False
            arbol.derecha = arbol.def_variables
            #print(arbol.derecha)
            funcion = arbol.funcion
            id = arbol.def_variables.identificador
            tipodato = arbol.def_variables.tipo
            if self.busca_simbolo(id,tipodato,DEFINICIONVAR,funcion) == False:
                obj = Semantico()
                obj.tipo = 'variable'
                obj.tipo_dato = tipodato
                obj.nombre = id
                obj.funcion = funcion
                self.tabla_simbolos.append(obj)
                arbol.valido = True
                arbol.derecha.valido = True
            else:
                arbol.valido = False
                arbol.derecha.valido = False
            #print(arbol.def_variables.__dict__)

            arbol_nuevo = arbol.def_variables
            arbol = arbol.def_variables
            while arbol.derecha != None:
                if arbol.derecha != None:
                    #print(arbol.derecha.__dict__)
                    id = arbol.derecha.identificador
                    if self.busca_simbolo(id,tipodato,DEFINICIONVAR,funcion) == False:
                        obj2 = Semantico()
                        obj2.tipo = 'variable'
                        obj2.tipo_dato = tipodato
                        obj2.nombre = id
                        obj2.funcion = funcion
                        self.tabla_simbolos.append(obj2)
                        arbol.derecha.valido = True
                        #print('Valido')
                    else:
                        #print('NO Valido')
                        arbol.derecha.valido = False
                        self.bandera = True
                        break


                    if arbol.derecha.valido == True:
                        arbol = arbol.derecha
                        arbol.valido = True
                    else:
                        arbol = arbol.derecha
                        arbol.valido = False
                    print(arbol.valido)

            print("BANDERA " + str(self.bandera))
            if self.bandera == True or arbol_nuevo.valido == False:
                return False
            else:
                return True
            print(arbol.valido)

        elif elemento == 'DefLocal_S':
            print(arbol.__dict__)
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Sentencia_return':
            print(arbol.__dict__)
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'ValorRegresa':
            arbol.valido = True
            #print(arbol.__dict__)
            '''if arbol.derecha == None:
                if self.busca_simbolo(arbol.funcion,'void',FUNCION_REGRESA) == True:
                    arbol.valido = True
                else:
                    arbol.valido = False
            #else:
            #    arbol.valido = True
            print(arbol.__dict__)'''

        elif elemento == 'Sentencia_asignacion':
            tipo = arbol.derecha.tipo_elemento
            id = arbol.identificador
            result = self.busca_simbolo(id,None,VARIABLE,arbol.funcion)
            if result['band'] == False:
                arbol.valido = False
            else:
                if tipo == result['tipo']:
                    arbol.valido = True
                else:
                    arbol.valido = False

            print(arbol.valido)

        elif elemento == 'Sentencia_while':
            #arbol.valido = True
            print(arbol.__dict__)
            if arbol.derecha.valido == True and arbol.izquierda.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Sentencia_if':
            #print(arbol.__dict__)
            #print(arbol.izquierda.valido, arbol.derecha.valido, arbol.centro.valido)
            if arbol.izquierda.valido == True and arbol.derecha.valido == True:
                if arbol.centro.valido == True:
                    arbol.valido = True
                else:
                    arbol.valido = False
            else:
                arbol.valido = False

        elif elemento == 'SentenciaBloque_B':
            print(arbol.__dict__)
            #arbol.valido = True
            print(arbol.derecha.valido)
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Bloque':
            print(arbol.__dict__)
            print(arbol.derecha.valido)
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Sentencias':
            print(arbol.__dict__)
            #arbol.valido = True
            if arbol.derecha == None and arbol.izquierda == None:
                arbol.valido = True
            elif arbol.derecha == None:             #No tiene deflocales
                if arbol.izquierda.valido == True:
                    arbol.valido = True
            else:
                print(arbol.derecha.valido, arbol.izquierda.valido)
                if arbol.derecha.valido == True and arbol.izquierda.valido == True:
                    arbol.valido = True
                else:
                    arbol.valido = False

        elif elemento == 'SentenciaBloque_S':
            print(arbol.__dict__)
            #arbol.valido = True
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False

        elif elemento == 'Sentencia_llamada':
            print(arbol.__dict__)
            if arbol.derecha.valido == True:
                arbol.valido = True
            else:
                arbol.valido = False
            arbol.valido = True

        elif elemento == 'LlamadaFuncion':
            arbol.valido = True
            print(arbol.__dict__)

        elif elemento == 'Otro':
            print(arbol.__dict__)
            if arbol.derecha == None:
                arbol.valido = True
            else:
                if arbol.derecha.valido == True:
                    arbol.valido = True
                else:
                    arbol.valido = False

        elif elemento == 'Expresion_doble':
            #arbol.valido = True
            print(arbol.__dict__)
            if arbol.izquierda.valido == True and arbol.derecha.valido == True:
                #print(arbol.izquierda.tipo_elemento, arbol.derecha.tipo_elemento)
                if arbol.izquierda.tipo_elemento == arbol.derecha.tipo_elemento:
                    arbol.valido = True
                    arbol.tipo_elemento = arbol.izquierda.tipo_elemento
                else:
                    arbol.valido = False
                    arbol.tipo_elemento = 'error'
            else:
                arbol.tipo_elemento = 'error'
                arbol.valido = False
            #print(arbol.izquierda.valido, arbol.derecha.valido)

        elif elemento == 'Expresion_Termino':
            arbol.valido = True
            if arbol.derecha.valido == True:
                arbol.valido = True
                arbol.tipo_elemento = arbol.derecha.tipo_elemento
            else:
                arbol.valido = False
                arbol.tipo_elemento = 'error'
            print(arbol.__dict__)

        elif elemento == 'Termino_entero':
            if arbol.elemento != None:
                arbol.valido = True
                arbol.tipo_elemento = 'int'
            print(arbol.__dict__)

        elif elemento == 'Termino_cadena':
            if arbol.elemento != None:
                arbol.valido = True
                arbol.tipo_elemento = 'cadena'
            print(arbol.__dict__)

        elif elemento == 'Termino_id':
            arbol.valido = True
            result = self.busca_simbolo(arbol.elemento,None,VARIABLE,arbol.funcion)
            if result['band'] == False:
                arbol.valido = False
            else:
                arbol.valido = True
                arbol.tipo_elemento = result['tipo']
            print(arbol.__dict__)

        elif elemento == 'Termino_real':
            if arbol.elemento != None:
                arbol.valido = True
                arbol.tipo_elemento = 'float'
            print(arbol.__dict__)

        elif elemento == 'Expresion':
            print(arbol.__dict__)
            if arbol.derecha.valido == True:
                arbol.valido = True
                arbol.tipo_elemento = arbol.derecha.tipo_elemento
            else:
                arbol.valido = False
                arbol.tipo_elemento = 'error'












#
