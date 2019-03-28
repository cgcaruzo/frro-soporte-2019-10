# Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.
def sumatoria(n):
	sum = 0
	for x in range(1,n+1):
		sum += x
	return sum

assert(sumatoria(5) == 15)
assert(sumatoria(3) == 6)

x = int(input("Ingrese un número: "))
print(sumatoria(x))

