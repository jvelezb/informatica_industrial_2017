class Vehiculo:    
	nombre= ""
	tipo= "car"
	color = ""
	precio= 100.00
	def description(self):
		desc_str = "El %s es %s %s y su precio $%.2f." % (self.nombre, self.color, self.tipo, self.precio)
		return desc_str

car1 = Vehiculo()
car2 = Vehiculo()
car1.nombre = "Vocho"
car2.nombre = "Ferrari"
car1.color = "Blanco"
car2.color = "Rojo"
car2.precio = 100000
print(car1.description())
print(car2.description())
