class Alumno:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def imprimeNombre(self):
        print("Name  = " + self.name)

    def estudia(self):
    	print("El alumno(padre) -->",self.name)

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

    def estudia(self):
    	print("El alumno (hijo) -->",self.name)


class AlumnoMaster(AlumnoIMT, Profesor):

	def __init__(self,nombre,clases):
		Profesor.__init__(self,clases)
		AlumnoIMT.__init__(self,nombre)

	def imprimeNombre(self):
		print("Este es un super alumno  = " + self.name)



 
brian = Alumno("Brain")
#brian.imprimeNombre()
#brian.estudia()
mario = Alumno("Mario")

diana = AlumnoIMT("Diana")
#diana.imprimeNombre()
#diana.programa()
#diana.estudia()

daniel = AlumnoIMT("Daniel")
salon = [brian,diana,mario, daniel]

# for estudiante in salon:
# 	estudiante.estudia()


juan = Profesor(["informatica","mate"])
# juan.imprimirClases()


clases = ["informatica industrial", "arquitectura","web","mate 1"]
superAlumno = AlumnoMaster("Juan", clases)
superAlumno.imprimeNombre()
superAlumno.estudia()
print("se imprimen clases")
superAlumno.imprimirClases()







