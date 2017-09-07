archivo = open("archivo5.txt","r")
contador = 0 
linea= archivo.read()
archivo = open("archivo5.txt","w")
if len(linea) ==0:
	print("archivo nuevo")
	archivo.write("0")
else:
	contador = int(linea) +1
	print("valor de contador: ",contador)
	archivo.write(str(contador))
archivo.close()