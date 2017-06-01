# -*- coding: utf-8 -*-

# Here we gonna create a interpreter.....

from subprocess import call

def read_doc():
    text = []
    a_file = input("what is the name of the file that we gonna use: ")
    the_file = open(a_file, 'r')
    for line in the_file:
        if len(line) > 0:
            text.append(line)
    return (text)

def esSimboloEsp(caracter):
    valido = True
    for c in caracter:
        if not c in ['+', '-', '*', ';', ',', '.', ':', '!', '=', '%', '&', '/', '(', ')', '[', ']', '<', '>']:
            valido = False
    return valido

def esSeparador(car):
    valido = True
    if not car == " ":
        valido = False
    return valido

def esEntero(cad):
    valido = True
    for c in cad:
        if c not in "0123456789":
            valido = False
    return valido

def esFlotante(cad):
    a=[]
    if cad[0]!="." and cad[-1]!="." and cad.count(".")==1:
        a = cad.split(".")
        if esEntero(a[0]) and esEntero(a[1]):
            return True
        else:
            return False
    return True

def esId(cad):
    if cad[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
        return True
    else:
        return False

def esTipo(cad):
    if cad in ["int", "float", "string", "boolean"]:
        return True
    return False


def separaTokens(linea):
    tokens = []
    tokens2 = []
    dentro = False
    for l in linea:
        if esSimboloEsp(l) and not(dentro):
            tokens.append(l)
        if (esSimboloEsp(l) or esSeparador(l)) and dentro:
            tokens.append(cad)
            dentro = False
            if esSimboloEsp(l):
                tokens.append(l)
        if not (esSimboloEsp(l)) and not (esSeparador(l)) and not(dentro):
            dentro = True
            cad=""
        if not (esSimboloEsp(l)) and not (esSeparador(l)) and dentro:
                cad = cad + l
    compuesto = False
    for c in range(len(tokens)-1):
        if compuesto:
            compuesto = False
            continue
        if tokens[c] in ":<>!" and tokens[c+1]=="=":
            tokens2.append(tokens[c]+"=")
            compuesto = True
        else:
            tokens2.append(tokens[c])
    tokens2.append(tokens[-1])
    for c in range(1,len(tokens2)-1):
        if tokens2[c]=="." and esEntero(tokens2[c-1]) and esEntero(tokens2[c+1]):
            tokens2[c]=tokens2[c-1]+tokens2[c]+tokens2[c+1]
            tokens2[c-1]="borrar"
            tokens2[c+1]="borrar"
    porBorrar = tokens2.count("borrar")
    for c in range(porBorrar):
        tokens2.remove("borrar")
    return tokens2

def print_1(parameter, *args):
    msj = print(parameter, *args)
    return msj

def clear(arg):
    return call(arg)
