lista = ['Alberto',23,23,'Zapata',43,'Carlos','Alejandro','Claudia','Mariana',2,1,4,342]
print(lista)
for i in range(0,len(lista)):
	print("lista:",lista[i],'i: ',i)
	if lista[i] != str:
		lista[i] = str(lista[i])

print (lista)
lista.sort()
#listaNum.sort(reverse= True)
print(lista)
#print(listaNum)