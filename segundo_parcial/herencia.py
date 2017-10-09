class Alumno:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def imprimeNombre(self):
        print("Name  = " + self.name)

class Profesor:
	def __init__(self, clases):
		
		self.clases = clases

	def imprimirClases(self):
		for clase in self.clases:
			print(clase)

class AlumnoIMT(Alumno):
 
    def __init__(self, name):
        self.name = name

    def programa(self):
        print("programa Python")

class AlumnoMaster(AlumnoIMT, Profesor):

	def __init__(self,nombre,clases):
		Profesor.__init__(self,clases)
		AlumnoIMT.__init__(self,nombre)

	def imprimeNombre(self):
		print("Este es un super alumno  = " + self.name)

 
brian = Alumno("Fernando")
brian.imprimeNombre()

diana = AlumnoIMT("Diana")
diana.imprimeNombre()
diana.programa()

clases = ["informatica industrial", "arquitectura","web","mate 1"]
superAlumno = AlumnoMaster("Juan", clases)
superAlumno.imprimeNombre()
print("se imprimen clases")
superAlumno.imprimirClases()
