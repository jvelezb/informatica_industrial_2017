from random import randint
diccionario = {"Nombre":"Juan","Apellido":"Velez","Materia":"Informatica industrial",'Edad':20, "Calificacion":{"informatica industrial":95,"Matematicas 1":50,"Fisica 1":79}}
listado =[1,2,3,5,2,5,"dfsd","fsd"]
print("listado: ",listado[3])
print("Name: ",diccionario["Nombre"])
print("Apellido: ",diccionario["Apellido"])
print("edad: ",diccionario["Edad"])
print("calificaciones mate 1: ",	diccionario["Calificacion"]["Matematicas 1"])
dict2 =  diccionario.copy()
#print(dict2)
dict3 = diccionario.fromkeys(["Nombre","Edad"])
dict3["Nombre"] = input("Nombre")
print(dict3)
dict3.clear()
print(dict3)
#print(dict2)
#del dict2
#print(dict2)
diccionario.pop("Materia",None)
#print(diccionario)
diccionario["Apellido Materno"] ="Ballesteros"
#print(diccionario)
print(diccionario.items())














