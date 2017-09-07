archivo = open("archivo.txt","r")
##wb = abre el archivo en formato binario / sin no existe lo crea.
#w = lo abre para escritura
## w+ = lectura y escritura
##a lo abre para añadir
## ab lo abre para añadir en formato binario
## r = lectura solamente
print("Nombre del archivo: ",archivo.name)
print("Modo: ", archivo.mode)
print("Abierto o cerrado", archivo.closed)
linea = archivo.readlines()
archivo.close()

print(linea)
