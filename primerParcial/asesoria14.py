str1 = "Juan Velez"
lista = list(str1)
lista.reverse()
##nueva = "".join(str(x) for x in lista)
nueva = ""
for x in lista:
	nueva = nueva +x
print(nueva)

str2 = "Hola mundo"
strNueva = ""
for x in str2:
	strNueva = x +strNueva
print(strNueva)

str3 = "Voy a reprobar --Mario--"
strNueva2 = ""
for x in range(len(str3)-1,-1,-1):
	strNueva2 = strNueva2 + str3[x]
print(strNueva2)