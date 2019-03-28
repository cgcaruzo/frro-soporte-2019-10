def inversa(cadena):
    resultado = ''
    for c in range(len(cadena)-1, -1, -1):
        resultado = resultado + cadena[c]
    return resultado

assert(inversa('abcdef') == 'fedcba')
