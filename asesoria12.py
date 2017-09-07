def imprimir_matriz(matriz):
	for x in matriz:
		renglon = ""
		for y in x:
			renglon = renglon +" "+ str(y)
		print(renglon)

def main():
	dimension = int(input("dimesion: "))
	matriz = []
	for x in range(dimension):
		matriz.append([])
		for y in range(dimension):
			matriz[x].append((y+1)*(x+1))
	imprimir_matriz(matriz)


