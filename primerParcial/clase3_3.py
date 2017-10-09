numero = 3
if numero%2 == 0:
	print("par")
else:
	print("impar") 

if numero %2 == 0 or numero% 4==0:
	print ("es multiplo de 2 o 4")
elif numero % 3 ==0 and numero%6 ==0:
	print("es multiplo de 3 y 6")
elif numero != 3:
	print("No es tres")
elif not numero%5==0:
	print("no es multiplo de 5")
else:
	print("otra cosa")  

