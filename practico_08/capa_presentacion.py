from funciones import *

r = obtenerTiempoAgotado(50, 5)

cant = 10000
sum = 0
for h in range(cant):
	sum = sum + obtenerTiempoAgotado(50,5)

res = sum / cant
print(res)