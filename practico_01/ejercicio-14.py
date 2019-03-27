# Programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo
# en cuenta que el laberinto se tomó como entrada y que es una matriz de valores
# True, False, (x,y) , donde True indica un obstáculo, False una celda donde se puede
# caminar, (x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del
# laberinto . 

matrix = [[True, True, True, True, True, True, True, True], [False, False, False, False, False, False, False, True], [True, False, False, True, False, True, True, True], [True, True, False, True, False, False, False, True], [True, True, False, True, False, True, False, True], [ True, True, False, False, False, False, False, False ], [True, True, True, True, True, True, True, True]]

for col in matrix:
	for el in col:
		if el:
			print(1)
		else:
			print(0)
	print('\n')