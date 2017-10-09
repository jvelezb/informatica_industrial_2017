lista =["juan","pedro","luisa",23,3,23,12,32,423,31,True]
print(type(lista))
for x in range(0,len(lista)):
	if type(lista[x]) == str:
		print(lista[x],"es string")
	elif type(lista[x]) == int:
		print(lista[x],"es entero")
		lista[x]= str(lista[x])
	else:
		print("es otra cosa")
		lista[x]= str(lista[x])

print(lista)
lista.sort(reverse=True)
print(lista)
