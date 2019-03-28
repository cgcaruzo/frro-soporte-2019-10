def inversa(cadena):
    resultado = ''
    for c in range(len(cadena)-1, -1, -1):
        resultado = resultado + cadena[c]
    return resultado

def es_palindromo(pal):
    lap = inversa(pal)
    if (pal == lap):
        return True
    else:
        return False

assert(es_palindromo('anitalavalatina') == True)
