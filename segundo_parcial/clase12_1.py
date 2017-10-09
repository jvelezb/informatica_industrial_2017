class Alumno:
	'Esta clase es la base de todos los alumnos'



	def __init__(self,nombre, matricula):
		self.nombre = nombre
		self.matricula = matricula

	def estudiar(self):
		print("El alumno estudia")

	def comer(self, comida):
		print("El alumno come:", comida)

	def imprimir(self):
		print("Nombre: ",self.nombre, "\n Matricula:", self.matricula)

mario = Alumno("Luis Mario","1234567")
luis = Alumno("Luis D","5858585858")

mario.estudiar()
luis.estudiar()
mario.comer("Papas")
luis.comer("Pizza")
mario.imprimir()
luis.imprimir()















