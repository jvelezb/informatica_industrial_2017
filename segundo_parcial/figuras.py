from abc import ABC, abstractmethod
import math

class Figura(ABC):
	@abstractmethod
	def obtenerArea(self):
		pass


	@abstractmethod
	def obtenerPerimetro(self):
		pass

class Poligono(Figura):
	pass
	

class Circulo(Figura):
	def __init__(self,radio):
		self.radio = radio

	def obtenerArea(self):
		return(math.pi * math.pow(self.radio,2))
	def obtenerPerimetro(self):
		return math.pi * 2 * self.radio

class Cuadrado (Poligono):
	pass



opcion = input("dame 1 si es circulo 2 si es rectangulo")
if ocion ==1
	figura = Ciruclo()
elfi opcion ==2
	figura = rectangulo()
circulo = Circulo(1)
print(circulo.obtenerPerimetro())
print(circulo.obtenerArea() )

#poli = Poligono()	
figura = Figura()	