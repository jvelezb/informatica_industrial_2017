x = [1,2,3,2,6,"hola",True, "como estas"]
print(x)
print(x[5],x[7])
print("TAMAÑO:",len(x))
print("TAMAÑO DE hola:",len(x[5]))
print(x[0:4])
x.insert(1,"saludos")
print(x)
x.append(False)
print(x)
x[1] = "adios"
print(x)
x.extend([34,34523,"dsd",3534,232,])
print(x)
x.append(12)
print(x)
x.pop()
print(x)
x.pop()
print(x)
x.remove("adios")
print(x)
x.remove(2)
x.remove(2)
print(x)
x.remove(x[0])
print(x)
print("Hola: ",x.index("hola"))
if "hola" in x:
	print("\nsi hay un hola")
else:
	print("no hay un hola")
print("Range: ",type(range(5)))
for i in range(5):
	print(i)
for i in x:
	print(i)
for index,item in enumerate(x):
	print(index,item)

























































