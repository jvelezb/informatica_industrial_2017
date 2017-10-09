class Automovil:
	def __init__(self): 
		self.__actualizacion()

	def manejar(self): 
		print('manejando')

	def __actualizacion(self): 
		print('se actualiza el auto')



vocho = Automovil() 
vocho.manejar() 
#vocho.__actualizacion()#no se puede acceder
