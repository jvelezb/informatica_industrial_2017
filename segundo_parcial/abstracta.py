from abc import ABC, abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def comer(self):
        print("El animal come")

    @abstractmethod
    def caminar(self):
        print("El animal camina")
        
class Tiburon(Animal):
    
    def comer(self):
        super().comer()
        print("El tiburon come en el mar")

    def caminar(self):
    	print("El tiburon nada")
        
class Mamifero(Animal):
	pass

class Elefante(Mamifero):
	def comer(self):
		super().comer()
		print("el Elefante come")

	def caminar(self):
		print("El elefante camina lento")

tiburonBlanco = Tiburon()
dumbo = Elefante()

dumbo.comer()
print("a darle hacer ejercicio")
dumbo.caminar()
tiburonBlanco.caminar()

animal = Animal()
#mamifero = Mamifero()
print("Viene el ciclo for: ")
zoo = [tiburonBlanco, dumbo]
for animal in zoo:
    animal.comer()









