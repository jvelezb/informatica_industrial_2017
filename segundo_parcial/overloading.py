
class Alumno:
 
    def decirHola(self, name=None):
        if name is not None:
            print('Hola ' + name)
        else:
            print('Hola ')
 
al1 = Alumno()
 
al1.decirHola()
 
# Call the method with a parameter
al1.decirHola('Luis Mario')