archivo = open("archivo.txt","r")
for linea in archivo:
	if "Hola" in linea:
		print(linea)