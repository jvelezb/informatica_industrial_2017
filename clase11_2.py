#archivo = open("archivo.txt","r")
##wb = abre el archivo en formato binario / sin no existe lo crea.
#w = lo abre para escritura
## w+ = lectura y escritura
##a lo abre para añadir
## ab lo abre para añadir en formato binario
## r = lectura solamente
with open("archivo.txt") as archivo:
	datos= archivo.read()
	print(datos)
archivo.close()