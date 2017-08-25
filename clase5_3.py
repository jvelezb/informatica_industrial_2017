from functools import reduce

producto = 1
listq = [1,2,3,4,5]
for num in listq:
	producto = producto *num
print(producto)

producto2 = reduce((lambda x,y: x*y),[1,2,3,4,5])
print(producto2)
str = input("captura algo")
try:
	numero = int(str)

except:
	print("capturas algo que no es numero")
	lista =[12]
	numero = 0
lista1 = range(-5,numero)
print("lista original",list(lista1))
lista_menor_a_cero = list(filter(lambda x: x<=5,lista1))
print(lista_menor_a_cero)











