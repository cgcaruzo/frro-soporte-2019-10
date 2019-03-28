# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga
def mas_larga(lista):
	maxima_longitud = 0
	for palabra in lista:
		if len(palabra) > maxima_longitud:
			resultado = palabra
			maxima_longitud = len(palabra)
	return resultado

assert(mas_larga(['roberto', 'casa', 'pc', 'esdrujula']) == 'esdrujula')
assert(mas_larga(['roberto', 'casa', 'pc']) == 'roberto')
assert(mas_larga(['casa', 'pc']) == 'casa')