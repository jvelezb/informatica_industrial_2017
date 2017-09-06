lista = ['Alberto',23,23,True,'Zapata',43,'Carlos','Alejandro','Claudia','Mariana',2,1,4,342]
listaLetra = []
listaNumero = []
for x in lista:
	if type(x) ==str:
		listaLetra.append(x)
	elif type(x) == int:
		listaNumero.append(x)
	else:
		print("tengo algo que no conozco: ",x, "y su tipo: ",type(x))
listaLetra.sort()
listaNumero.sort()
listaNuevaOrdenada = []
listaNuevaOrdenada.append(  listaLetra)
listaNuevaOrdenada.append(listaNumero)
print(listaNuevaOrdenada)
	