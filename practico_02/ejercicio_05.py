# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    diccionario = {}
    for estudiante in estudiantes:
        if estudiante.carrera in diccionario:
            diccionario[estudiante.carrera] = diccionario[estudiante.carrera] + 1
        else:
            diccionario[estudiante.carrera] = 1
    return diccionario

a = Estudiante('ISI', 2008, 35, 25)
b = Estudiante('ISI', 2008, 35, 25)
c = Estudiante('ISI', 2008, 35, 25)
d = Estudiante('ISI', 2008, 35, 25)
e = Estudiante('QUIMICA', 2008, 35, 25)
f = Estudiante('QUIMICA', 2008, 35, 25)
g = Estudiante('CIVIL', 2008, 35, 25)
h = Estudiante('CIVIL', 2008, 35, 25)
i = Estudiante('CIVIL', 2008, 35, 25)
j = Estudiante('MECANICA', 2008, 35, 25)
k = Estudiante('ELECTRICA', 2008, 35, 25)
l = Estudiante('ELECTRICA', 2008, 35, 25)

lista = [a,b,c,d,e,f,g,h,i,j,k,l]


assert(organizar_estudiantes(lista) == {'ISI': 4, 'QUIMICA': 2, 'CIVIL': 3, 'MECANICA': 1, 'ELECTRICA': 2})
