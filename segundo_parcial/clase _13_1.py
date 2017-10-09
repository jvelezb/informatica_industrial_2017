class Alumno: 
	"""estamos creando una clase nueva para comprobar
	los elementos agregacion la composicon y herencia"""

	cuentaAlumnos = 0

	def __init__(self, nombre, matricula, carrera):
		print("Creando un alumno")
		self.nombre = nombre
		self.mat = matricula
		self.carrera = carrera
		Alumno.cuentaAlumnos += 1

	def displayNombre(self):
		print("nombre: ",self.nombre)

	def obtenerTotalAlumnos(self):
		print("el total de alumnos creados es:",Alumno.cuentaAlumnos)

	def obtenerTotal2(self):
		return Alumno.cuentaAlumnos

	def __del__(self):
		#print("Entrando a destruir alumnos")
		Alumno.cuentaAlumnos -=1

class AlumnoIMT(Alumno):
	def __init__(self):
		print("Creando un IMT")
		Alumno.cuentaAlumnos+=1


	
al1 = Alumno("Juan ","4323","LEM")
al2 = Alumno("Juan 2",322,"IIS")
al1.displayNombre()
al1.semestre = 2
print("El semestre,",al1.semestre)
atributoSemA2 =hasattr(al2,"semestre")
print("El semestre, al2",atributoSemA2)
atributoSemA1 =hasattr(al1,"semestre")
print("El semestre al1,",atributoSemA1)
print("el metodo de getattr2 es: ",getattr(al1,"semestre"))
setattr(al2,"salon",4213)
print("al2",getattr(al2,"salon"))
al1.obtenerTotalAlumnos()
al2.obtenerTotalAlumnos()
#print("EL total:",al1.obtenerTotal2())
#print("Alumnos", Alumno.__doc__)
#print("Nombre de la clase", Alumno.__name__)
#print("modulo: ",Alumno.__module__)
#print("base: ", Alumno.__base__)
#print("dict",Alumno.__dict__)
#del al1
#print("Total de objetos: ",al2.obtenerTotal2())
imt1 = AlumnoIMT()
imt1.obtenerTotalAlumnos()
imt1.nombre = "Mario"
imt1.displayNombre()





























