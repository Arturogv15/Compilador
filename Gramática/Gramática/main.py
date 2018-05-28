from pila import Pila as pila
from Lexico import Lexico as lexico
from Sintactico import TablaLR as sintactico

LR = sintactico()
p = pila()
p_codigo = pila()
lex = lexico

def main():
    lexico_flag = lex.sig_simbolo(lex)
    if lexico_flag == True:
        entrada = lex.simbolos
        tipo_entrada = lex.tipos
        p.push('$')
        p.push(0)
        p_codigo.push('$')
        p_codigo.push(0)
        arbol = LR.recorrer_entrada(entrada,tipo_entrada,p,p_codigo)
        if LR.correcto == True:
            arbol.postorden(arbol.lista_arbol[0])
            if arbol.lista_arbol[0].valido == False:
                print('Semanticamente no es correcto')
            else:
                print('EL CÓDIGO ES CORRECTO\n')
                #arbol.imprime()
        else:
            print('No valido sintácticamente')
    else:
        print('No valido léxicamente')


    print("\n")

if __name__ == '__main__':
    main()
