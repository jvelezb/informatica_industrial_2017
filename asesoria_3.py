lista = ['Alberto','Zapata','Carlos','Alejandro','Claudia','Mariana',2,1,4,342]
print(lista)
for i in range(0,len(lista)):
	print("lista:",lista[i],'i: ',i)
	valor = lista[i]
	if valor != str:
		lista.remove(valor)
		if(i<len(lista)):
			lista.insert(i,str(valor))
		else:
			lista.append(str(valor))

print (lista)
#lista.sort()
#listaNum.sort(reverse= True)
print(lista)
#print(listaNum)