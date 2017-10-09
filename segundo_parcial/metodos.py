class Vehiculo:    
	nombre= ""
	tipo= "car"
	color = ""
	precio = 500.00

	def description(self):
		desc_str = "El %s es %s %s y su precio $%.2f." % (self.nombre, self.color, self.tipo, self.precio)
		return desc_str


car1 = Vehiculo() ##intancia car1
car2 = Vehiculo() ##intancia car2

car1.nombre = "Vocho"
car2.nombre = "Ferrari"

car1.color = "Blanco"
car2.color = "Rojo"

car2.precio = 100000
car1.tipo = "economico"
car2.tipo = "deportivo"
car1.precio = 333

car1.numeroVelocidades = 4
car2.numeroVelocidades = 6

print(car1.description())
print(car2.description())
print("Velocidades Vocho: ",car1.numeroVelocidades)
print("Velocidades Ferrari: ",car2.numeroVelocidades)
