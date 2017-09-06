

def obtencion_diccionario(min,max,paso):
	diccionario = {}
	for x in range(min,max+1,paso):
		diccionario[x]=x*x
	return diccionario

pepito()

def pepito():
	minimo =int(input("Minimo: "))
	maximo = int(input("Maximo: ")) 
	escalon = int(input("Escalon"))
	d1 = obtencion_diccionario(minimo,maximo,escalon)
	print(d1)


#print(obtencion_diccionario(1,3,1))