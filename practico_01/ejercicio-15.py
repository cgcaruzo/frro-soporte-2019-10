#aReescriba el programa que pide al usuario una lista de números
# e imprime en pantalla el máximo y mínimo de los números introducidos al final, cuando el usuario introduce “fin”.
def max(lista):
    nummax= lista[0]
    for i in range(len(lista)):
        if nummax<lista[i]:
            nummax = lista[i]
        else:
            pass
    return nummax

def min(lista):
    nummin= lista[0]
    for i in range(len(lista)):
        if lista[i]<nummin:
            nummin = lista[i]
        else:
            pass
    return nummin

#list=[1110,2,3,4,4,110,1]
#ma= max(list)
#mi= min(list)
#print(mi, ma)

#b Escriba ahora el programa de modo que almacene los números que el usuario introduzca en una lista y usa
# las funciones max () y min () para calcular los números máximo y mínimo después de que el bucle termine.

def ingreso():
    x=0
    lista1= [int(input("Ingrese numero"))]
    while x != 'fin':
        x= input("Ingrese numero (o fin)")
        if x=='fin':
            break
        lista1.append(int(x))
    #print(lista1)
    return lista1

listausuario = ingreso()

print('Min:', min(listausuario), 'Max:', max(listausuario))
