def imprimir_matriz(matriz):
	for x in matriz:
		renglon = ""
		for y in x:
			renglon = renglon +" "+ str(y)
		print(renglon)

def main():
	dimensionx = int(input("dimesionx: "))
	dimensiony = int(input("dimesiony: "))
	matriz = []
	for x in range(dimensionx):
		matriz.append([])
		for y in range(dimensiony):
			matriz[x].append((y+1)*(x+1))
	imprimir_matriz(matriz)
main()

