# Definir una función superposicion() que tome dos listas y devuelva True si tienen al
# menos 1 miembro en común o devuelva False de lo contrario. Escribir la función
# usando el bucle for anidado.

def superposicion(lista1, lista2):
    for x in lista1:
    	for y in lista2:
    		if x == y:
    			return True
    return False

assert(superposicion([1,2,3,4,5], [9,6,7,8]) == False)
assert(superposicion([1,2,3,4,5], [4,6,7,8]) == True)
