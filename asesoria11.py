lista =["juan","pedro","luisa",234.324,4324.23,45.3,23,3,23,12,32,423,31,True]
listaNum = []
listaStr = []

for x in lista:
	if type(x)== str:
		listaStr.append(x)
	if type(x)== int or type(x)==float:
		listaNum.append(x)
print(listaStr)
print(listaNum)
listaStr.sort()
listaNum.sort()
print(listaStr)
print(listaNum)
listaNueva = listaStr+ listaNum 
print(listaNueva)
