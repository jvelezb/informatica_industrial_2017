class Automovil:
	__velocidadMaxima = 0 
	__nombre = ""

	#def __init__(self): 
	#	self.__velocidadMaxima = 200 
	#	self.__nombre = "Supercar"

	def __init__(self,velocidad = None):
		if velocidad is not None:
			self.__velocidadMaxima = velocidad
		else:
			self.__velocidadMaxima = 200


	def  manejar(self): 
		print ('Velocidad Maxima ' + str(self.__velocidadMaxima ) )

	def setVelocidadMaxima(self,speed):
		self.__velocidadMaxima = speed

	def getVelocidadMaxima(self):
		return self.__velocidadMaxima


def main():
	velocidad = int(input('dame la velocidad de auto'))
	vocho = Automovil()
	ferrari = Automovil(400)
	vocho.manejar()
	#vocho.__velocidadMaxima = 10000000000 # No se puede acceder
	#vocho.manejar()
	vocho.setVelocidadMaxima(velocidad)
	vocho.manejar()
	print("velocidad--> getter: ", vocho.getVelocidadMaxima())
	print("velocidad maxima ",ferrari.getVelocidadMaxima())


main()
