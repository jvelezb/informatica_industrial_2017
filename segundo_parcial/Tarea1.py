

from abc import ABC, abstractmethod


class Hogar(ABC):
	pass

class Departamento (Hogar):
	pass

class Casa(Hogar):
	pass

class Animales(ABC):
	pass

class Perro(Animal):
	pass

class Gato(Animal):
	pass

class Pajaro(Animal):
	pass

class Mujer:

	def __init__(self):
		self.animales = [] 


	def setHogar(self,hogar):
		self.hogar = hogar

	def addAnimales(animal):
		if type(self.hogar)== Casa and (type(animal) == Gato or  type(animal) == Perro):
			self.animales.append(animal)
		elif type(self.hogar)== Departamento and (type(animal) == Perro or  type(animal) == Pajaro):
			self.animales.append(animal)
		else:	
			print("no se agrego el animal")


def main():
	






