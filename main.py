# def waiting(order):
#     if order = a_input:
#         return True
#     return

from interpreter import *

waiting = False
recip = ""
var_1 = {}
var_2 = {}
var_3 = {}
var_4 = {}
var_5 = {}
var_6 = {}
var_7 = {}
var_8 = {}
var_9 = {}
var_10 = {}

while not recip == ["exit"]:
    recip = input("> ")
    recip = recip.split()  # Manejo a los inputs como listas para su mejor control

    if esEntero(recip):
        print ("Es entero")
    elif recip != ['']:  # Limpia la pantalla
        if recip[0] == 'clear':
            clear(recip[0])

        elif recip[0] == 'read':
            value = read()
            if type(value) == int:
                if recip[1] in var_1.keys():
                    if type(var_1[recip[1]]) == int:
                        var_1[recip[1]] = value
                        print(var_1)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_2.keys():
                    if type(var_2[recip[1]]) == int:
                        var_2[recip[1]] = value
                        print(var_2)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_3.keys():
                    if type(var_3[recip[1]]) == int:
                        var_3[recip[1]] = value
                        print(var_3)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_4.keys():
                    if type(var_4[recip[1]]) == int:
                        var_4[recip[1]] = value
                        print(var_4)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_5.keys():
                    if type(var_5[recip[1]]) == int:
                        var_5[recip[1]] = value
                        print(var_5)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_6.keys():
                    if type(var_6[recip[1]]) == int:
                        var_6[recip[1]] = value
                        print(var_6)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_7.keys():
                    if type(var_7[recip[1]]) == int:
                        var_7[recip[1]] = value
                        print(var_7)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_8.keys():
                    if type(var_8[recip[1]]) == int:
                        var_8[recip[1]] = value
                        print(var_8)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_9.keys():
                    if type(var_9[recip[1]]) == int:
                        var_9[recip[1]] = value
                        print(var_9)
                    else:
                        print('Se esperaba entero y se recibio string')
                elif recip[1] in var_10.keys():
                    if type(var_10[recip[1]]) == int:
                        var_10[recip[1]] = value
                        print(var_10)
                    else:
                        print('Se esperaba entero y se recibio string')
            elif type(value) == str:
                if recip[1] in var_1.keys():
                    if type(var_1[recip[1]]) == str:
                        var_1[recip[1]] = value
                        print(var_1)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_2.keys():
                    if type(var_2[recip[1]]) == str:
                        var_2[recip[1]] = value
                        print(var_2)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_3.keys():
                    if type(var_3[recip[1]]) == str:
                        var_3[recip[1]] = value
                        print(var_3)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_4.keys():
                    if type(var_4[recip[1]]) == str:
                        var_4[recip[1]] = value
                        print(var_4)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_5.keys():
                    if type(var_5[recip[1]]) == str:
                        var_5[recip[1]] = value
                        print(var_5)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_6.keys():
                    if type(var_6[recip[1]]) == str:
                        var_6[recip[1]] = value
                        print(var_6)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_7.keys():
                    if type(var_7[recip[1]]) == str:
                        var_7[recip[1]] = value
                        print(var_7)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_8.keys():
                    if type(var_8[recip[1]]) == str:
                        var_8[recip[1]] = value
                        print(var_8)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_9.keys():
                    if type(var_9[recip[1]]) == str:
                        var_9[recip[1]] = value
                        print(var_9)
                    else:
                        print('Se esperaba string y se recibio entero')
                elif recip[1] in var_10.keys():
                    if type(var_10[recip[1]]) == str:
                        var_10[recip[1]] = value
                        print(var_10)
                    else:
                        print('Se esperaba string y se recibio entero')
            else:
                print(type(value))
                print('Error de valor dado 3')


        elif recip[0] == 'print':  # imprimir en pantalla
            my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
            keys_list = []
            for dic in my_list:
                for e in dic:
                    keys_list.append(e)

            if recip[1] in keys_list:
                for dic in my_list:
                    if dic.get(recip[1]) != None:
                        print_1(dic.get(recip[1]))
            else:
                print_1(*recip[1:])

        elif 'var' in recip:  # Declarecion de variables
            if recip[1] == 'int':
                if var_1 == {}:
                    var_1[recip[2]] = 0
                    print(var_1)
                elif var_2 == {}:
                    var_2[recip[2]] = 0
                    print(var_2)
                elif var_3 == {}:
                    var_3[recip[2]] = 0
                    print(var_3)
                elif var_4 == {}:
                    var_4[recip[2]] = 0
                    print(var_4)
                elif var_5 == {}:
                    var_5[recip[2]] = 0
                    print(var_5)
                elif var_6 == {}:
                    var_6[recip[2]] = 0
                    print(var_6)
                elif var_7 == {}:
                    var_7[recip[2]] = 0
                    print(var_7)
                elif var_8 == {}:
                    var_8[recip[2]] = 0
                    print(var_8)
                elif var_9 == {}:
                    var_9[recip[2]] = 0
                    print(var_9)
                elif var_10 == {}:
                    var_10[recip[2]] = 0
                    print(var_10)
            elif recip[1] == 'string':
                if var_1 == {}:
                    var_1[recip[2]] = ''
                    print(var_1)
                elif var_2 == {}:
                    var_2[recip[2]] = ''
                    print(var_2)
                elif var_3 == {}:
                    var_3[recip[2]] = ''
                    print(var_3)
                elif var_4 == {}:
                    var_4[recip[2]] = ''
                    print(var_4)
                elif var_5 == {}:
                    var_5[recip[2]] = ''
                    print(var_5)
                elif var_6 == {}:
                    var_6[recip[2]] = ''
                    print(var_6)
                elif var_7 == {}:
                    var_7[recip[2]] = ''
                    print(var_7)
                elif var_8 == {}:
                    var_8[recip[2]] = ''
                    print(var_8)
                elif var_9 == {}:
                    var_9[recip[2]] = ''
                    print(var_9)
                elif var_10 == {}:
                    var_10[recip[2]] = ''
                    print(var_10)

                else:
                    print('Se terminaron las variables')
        elif '=' in recip:
            if recip[1] == '=' and len(recip) < 4:  # Asignacion de valores a las variables
                try:
                    recip[2] = int(recip[2])
                    if recip[0] in var_1.keys():
                        var_1[recip[0]] = recip[2]
                        print(var_1)
                    elif recip[0] in var_2.keys():
                        var_2[recip[0]] = recip[2]
                        print(var_2)
                    elif recip[0] in var_3.keys():
                        var_3[recip[0]] = recip[2]
                        print(var_3)
                    elif recip[0] in var_4.keys():
                        var_4[recip[0]] = recip[2]
                        print(var_4)
                    elif recip[0] in var_5.keys():
                        var_5[recip[0]] = recip[2]
                        print(var_5)
                    elif recip[0] in var_6.keys():
                        var_6[recip[0]] = recip[2]
                        print(var_6)
                    elif recip[0] in var_7.keys():
                        var_7[recip[0]] = recip[2]
                        print(var_7)
                    elif recip[0] in var_8.keys():
                        var_8[recip[0]] = recip[2]
                        print(var_8)
                    elif recip[0] in var_9.keys():
                        var_9[recip[0]] = recip[2]
                        print(var_9)
                    elif recip[0] in var_10.keys():
                        var_10[recip[0]] = recip[2]
                        print(var_10)
                    else:
                        print ('Error (ya no hay variables o no estan declaradas)')
                except:
                    if recip[0] in var_1.keys():
                        var_1[recip[0]] = recip[2]
                        print(var_1)
                    elif recip[0] in var_2.keys():
                        var_2[recip[0]] = recip[2]
                        print(var_2)
                    elif recip[0] in var_3.keys():
                        var_3[recip[0]] = recip[2]
                        print(var_3)
                    elif recip[0] in var_4.keys():
                        var_4[recip[0]] = recip[2]
                        print(var_4)
                    elif recip[0] in var_5.keys():
                        var_5[recip[0]] = recip[2]
                        print(var_5)
                    elif recip[0] in var_6.keys():
                        var_6[recip[0]] = recip[2]
                        print(var_6)
                    elif recip[0] in var_7.keys():
                        var_7[recip[0]] = recip[2]
                        print(var_7)
                    elif recip[0] in var_8.keys():
                        var_8[recip[0]] = recip[2]
                        print(var_8)
                    elif recip[0] in var_9.keys():
                        var_9[recip[0]] = recip[2]
                        print(var_9)
                    elif recip[0] in var_10.keys():
                        var_10[recip[0]] = recip[2]
                        print(var_10)
                    else:
                        print ('Error (ya no hay variables o no estan declaradas)')
            elif recip[1] == '=' and recip[3] == '+':  # Suma de variables mas asignacion al mismo tiempo
                my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
                keys_list = []
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[2] in keys_list and recip[4] in keys_list:
                    values = []
                    for dic in my_list:
                        if dic.get(recip[2]) != None:
                            values.append(dic.get(recip[2]))
                        elif dic.get(recip[4]) != None:
                            values.append(dic.get(recip[4]))
                    try:
                        v_1 = int(values[0]) + int(values[1])

                        if recip[0] in var_1.keys():
                            var_1[recip[0]] = v_1
                            print(var_1)
                        elif recip[0] in var_2.keys():
                            var_2[recip[0]] = v_1
                            print(var_2)
                        elif recip[0] in var_3.keys():
                            var_3[recip[0]] = v_1
                            print(var_3)
                        elif recip[0] in var_4.keys():
                            var_4[recip[0]] = v_1
                            print(var_4)
                        elif recip[0] in var_5.keys():
                            var_5[recip[0]] = v_1
                            print(var_5)
                        elif recip[0] in var_6.keys():
                            var_6[recip[0]] = v_1
                            print(var_6)
                        elif recip[0] in var_7.keys():
                            var_7[recip[0]] = v_1
                            print(var_7)
                        elif recip[0] in var_8.keys():
                            var_8[recip[0]] = v_1
                            print(var_8)
                        elif recip[0] in var_9.keys():
                            var_9[recip[0]] = v_1
                            print(var_9)
                        elif recip[0] in var_10.keys():
                            var_10[recip[0]] = v_1
                            print(var_10)
                        else:
                            print ('Error (ya no hay variables o no estan declaradas)')

                    except ValueError:
                        print('Error de valores')
                else:
                    print ('Una de las variables no esta declarada')

            elif recip[1] == '=' and recip[3] == '*':  # Multiplicacion de variables mas asignacion al mismo tiempo
                my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
                keys_list = []
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[2] in keys_list and recip[4] in keys_list:
                    values = []
                    for dic in my_list:
                        if dic.get(recip[2]) != None:
                            values.append(dic.get(recip[2]))
                        elif dic.get(recip[4]) != None:
                            values.append(dic.get(recip[4]))
                    try:
                        v_1 = int(values[0]) * int(values[1])
                        if recip[0] in var_1.keys():
                            var_1[recip[0]] = v_1
                            print(var_1)
                        elif recip[0] in var_2.keys():
                            var_2[recip[0]] = v_1
                            print(var_2)
                        elif recip[0] in var_3.keys():
                            var_3[recip[0]] = v_1
                            print(var_3)
                        elif recip[0] in var_4.keys():
                            var_4[recip[0]] = v_1
                            print(var_4)
                        elif recip[0] in var_5.keys():
                            var_5[recip[0]] = v_1
                            print(var_5)
                        elif recip[0] in var_6.keys():
                            var_6[recip[0]] = v_1
                            print(var_6)
                        elif recip[0] in var_7.keys():
                            var_7[recip[0]] = v_1
                            print(var_7)
                        elif recip[0] in var_8.keys():
                            var_8[recip[0]] = v_1
                            print(var_8)
                        elif recip[0] in var_9.keys():
                            var_9[recip[0]] = v_1
                            print(var_9)
                        elif recip[0] in var_10.keys():
                            var_10[recip[0]] = v_1
                            print(var_10)
                        else:
                            print ('Error (ya no hay variables o no estan declaradas)')
                    except ValueError:
                        print('Error de valores')
                else:
                    print ('Una de las variables no esta declarada')

            elif recip[1] == '=' and recip[3] == '-':  # Resta de variables mas asignacion al mismo tiempo
                my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
                keys_list = []
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[2] in keys_list and recip[4] in keys_list:
                    v_1 = 0
                    v_2 = 0
                    for dic in my_list:
                        if dic.get(recip[2]) != None:
                            try:
                                v_1 = dic.get(recip[2])
                            except:
                                pass
                        elif dic.get(recip[4]) != None:
                            try:
                                v_2 = dic.get(recip[4])
                            except:
                                pass

                    if type(v_1) == int and type(v_2) == int:
                        v_3 = v_1 - v_2

                        if recip[0] in var_1.keys():
                            var_1[recip[0]] = v_3
                            print(var_1)
                        elif recip[0] in var_2.keys():
                            var_2[recip[0]] = v_3
                            print(var_2)
                        elif recip[0] in var_3.keys():
                            var_3[recip[0]] = v_3
                            print(var_3)
                        elif recip[0] in var_4.keys():
                            var_4[recip[0]] = v_3
                            print(var_4)
                        elif recip[0] in var_5.keys():
                            var_5[recip[0]] = v_3
                            print(var_5)
                        elif recip[0] in var_6.keys():
                            var_6[recip[0]] = v_3
                            print(var_6)
                        elif recip[0] in var_7.keys():
                            var_7[recip[0]] = v_3
                            print(var_7)
                        elif recip[0] in var_8.keys():
                            var_8[recip[0]] = v_3
                            print(var_8)
                        elif recip[0] in var_9.keys():
                            var_9[recip[0]] = v_3
                            print(var_9)
                        elif recip[0] in var_10.keys():
                            var_10[recip[0]] = v_3
                            print(var_10)
                        else:
                            print ('Error (ya no hay variables o no estan declaradas)')
                    else:
                        print('Error de valores')

                else:
                    print ('Una de las variables no esta declarada')

            elif recip[1] == '=' and recip[3] == '/':  # Resta de variables mas asignacion al mismo tiempo
                my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
                keys_list = []
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[2] in keys_list and recip[4] in keys_list:
                    v_1 = 0
                    v_2 = 0
                    for dic in my_list:
                        if dic.get(recip[2]) != None:
                            try:
                                v_1 = dic.get(recip[2])
                            except:
                                pass
                        elif dic.get(recip[4]) != None:
                            try:
                                v_2 = dic.get(recip[4])
                            except:
                                pass

                    if type(v_1) == int and type(v_2) == int:
                        v_3 = v_1 / v_2

                        if recip[0] in var_1.keys():
                            var_1[recip[0]] = v_3
                            print(var_1)
                        elif recip[0] in var_2.keys():
                            var_2[recip[0]] = v_3
                            print(var_2)
                        elif recip[0] in var_3.keys():
                            var_3[recip[0]] = v_3
                            print(var_3)
                        elif recip[0] in var_4.keys():
                            var_4[recip[0]] = v_3
                            print(var_4)
                        elif recip[0] in var_5.keys():
                            var_5[recip[0]] = v_3
                            print(var_5)
                        elif recip[0] in var_6.keys():
                            var_6[recip[0]] = v_3
                            print(var_6)
                        elif recip[0] in var_7.keys():
                            var_7[recip[0]] = v_3
                            print(var_7)
                        elif recip[0] in var_8.keys():
                            var_8[recip[0]] = v_3
                            print(var_8)
                        elif recip[0] in var_9.keys():
                            var_9[recip[0]] = v_3
                            print(var_9)
                        elif recip[0] in var_10.keys():
                            var_10[recip[0]] = v_3
                            print(var_10)
                        else:
                            print ('Error (ya no hay variables o no estan declaradas)')
                    else:
                        print ('Error de valores')

                else:
                    print ('Una de las variables no esta declarada')
            else:
                print (recip[1])

        elif '+' in recip:
            my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
            keys_list = []
            if recip[1] == '+':  # Suma de variables [WIP: Solo suma dos numeros]
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[0] in keys_list and recip[2] in keys_list:
                    values = []
                    for dic in my_list:
                        if dic.get(recip[0]) != None:
                            values.append(dic.get(recip[0]))
                        elif dic.get(recip[2]) != None:
                            values.append(dic.get(recip[2]))
                    try:
                        print (int(values[0]) + int(values[1]))
                    except ValueError:
                        print('Error de valor')
                else:
                    print ('Una de las variables no esta declarada')
        elif '*' in recip:
            my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
            keys_list = []
            if recip[1] == '*':  # Multiplicacion de variables [WIP: Solo multiplica dos numeros]
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[0] in keys_list and recip[2] in keys_list:
                    values = []
                    for dic in my_list:
                        if dic.get(recip[0]) != None:
                            values.append(dic.get(recip[0]))
                        elif dic.get(recip[2]) != None:
                            values.append(dic.get(recip[2]))
                    try:
                        print (int(values[0]) * int(values[1]))
                    except ValueError:
                        print('Error de valores')
                else:
                    print ('Una de las variables no esta declarada')
        elif '-' in recip:
            my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
            keys_list = []
            if recip[1] == '-':  # Resta de variables [WIP: Solo resta dos numeros]
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[0] in keys_list and recip[2] in keys_list:
                    v_1 = 0
                    v_2 = 0
                    for dic in my_list:
                        if dic.get(recip[0]) != None:
                            try:
                                v_1 = dic.get(recip[0])
                            except:
                                pass
                        elif dic.get(recip[2]) != None:
                            try:
                                v_2 = dic.get(recip[2])
                            except:
                                pass
                    if type(v_1) == int and type(v_2) == int:
                        print (v_1 - v_2)
                    else:
                        print('Error de valores')
                else:
                    print('Una de las variables no esta declarada')
        elif '/' in recip:
            my_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
            keys_list = []
            if recip[1] == '/':  # Divicion de variables [WIP: Solo divide dos numeros]
                for dic in my_list:
                    for e in dic:
                        keys_list.append(e)
                if recip[0] in keys_list and recip[2] in keys_list:
                    v_1 = 0
                    v_2 = 0
                    for dic in my_list:
                        if dic.get(recip[0]) != None:
                            try:
                                v_1 = dic.get(recip[0])
                            except:
                                pass
                        elif dic.get(recip[2]) != None:
                            try:
                                v_2 = dic.get(recip[2])
                            except:
                                pass
                    if type(v_1) == int and type(v_2) == int:
                        print (v_1 / v_2)
                    else:
                        print('Error de valores')
                else:
                    print('Una de las variables no esta declarada')
            else:
                print('Error')
    # elif recip[1] == 'float':
    #         var_1 = recip[2]
    #     elif recip[1] == 'string':
    #         var_1 = recip[2]
    #     print ("Es una variable")
    # elif esSimboloEsp(recip):
    #     print ("Es un simbolo especial")
    # elif esSeparador(recip):
    #     print ("Es un separador")
    # elif esTipo(recip):
    #     print ("Es un tipo de dato")
    # # elif esFlotante(recip):
    # #     print ("Es un flotante")
    # elif esId(recip):
    #     print ("Es un ID")
    # else:
    #     print (recip[1])
    #     print (type(recip))
