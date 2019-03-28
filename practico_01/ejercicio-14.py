# Programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo
# en cuenta que el laberinto se tomó como entrada y que es una matriz de valores
# True, False, (x,y) , donde True indica un obstáculo, False una celda donde se puede
# caminar, (x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del
# laberinto . 

def resolver(laberinto,inicio, fin):

	def caminar(lab, x, y, a, b, vis):
		if x == a and y == b:
			return [(x,y)],vis

		if lab[x][y]:
			return [],vis

		vis.append((x,y))

		if x+1 <= len(lab)-1 and not lab[x+1][y] and (x+1, y) not in vis:
			camino, vis = caminar(lab, x+1, y, a, b, vis)
			if camino != []:
				return ([(x,y)]+camino, vis)

		if y+1 <= len(lab[0])-1 and not lab[x][y+1] and (x, y+1) not in vis:
			camino, vis = caminar(lab, x, y+1, a, b, vis)
			if camino != []:
				return ([(x,y)]+camino, vis)

		if x-1 >= 0 and not lab[x-1][y] and (x-1, y) not in vis:
			camino, vis = caminar(lab, x-1, y, a, b, vis)
			if camino != []:
				return ([(x,y)]+camino, vis)

		if y-1 >= 0 and not lab[x][y-1] and (x, y-1) not in vis:
			camino, vis = caminar(lab, x, y-1, a, b, vis)
			if camino != []:
				return ([(x,y)]+camino, vis)

		return [],vis

	x,y = inicio
	a,b = fin
	solucion, visitados = caminar(laberinto,x,y,a,b,[])
	return solucion


laberinto = [[True,True,True,True,True,True,True,True],
[False,False,False,False,False,False,False,True],
[True,False,False,True,False,True,False,True],
[True,True,True,True,False,True,True,True],
[True,False,False,True,False,False,False,True],
[True,True,False,False,False,True,False,False],
[True,True,True,True,True,True,True,True]]


inicio = (1,0)
fin = (5,7)

#print(resolver(laberinto,inicio,fin))
assert(resolver(laberinto,inicio,fin) == [(1, 0), (1, 1), (2, 1), (2, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (5, 7)])

