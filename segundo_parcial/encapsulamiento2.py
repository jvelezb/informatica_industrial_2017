class Automovil:
	__velocidadMaxima = 0 
	__nombre = ""

	def __init__(self): 
		self.__velocidadMaxima = 200 
		self.__nombre = "Supercar"

	def  manejar(self): 
		print ('Velocidad Maxima ' + str(self.__velocidadMaxima ) )

	def setVelocidadMaxima(self,speed):
		self.__velocidadMaxima = speed


vocho = Automovil()
vocho.manejar()
vocho.__velocidadMaxima = 10000000000 # No se puede aceder
vocho.manejar()
vocho.setVelocidadMaxima(100)
vocho.manejar()
print("velocidad: ", vocho.__velocidadMaxima)
