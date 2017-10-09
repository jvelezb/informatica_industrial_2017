class Alumno:
 
    def decirHola(self, name = None):
        if name is not None:
            print('Hola ' + name)
            self.name = name
        else:
            print('Hola ')

    def  estudiar(self):
    	print("Alumno estudiando")
 


al1 = Alumno()
 
al1.decirHola()
 
# Call the method with a parameter
al1.decirHola('Luis Mario')
print("Alumno nombre: ", al1.name)
al1.estudiar()
al2 = Alumno()
al2.decirHola()
print("Alumno nombre: ", al2.name)

