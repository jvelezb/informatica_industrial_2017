class Automovil:
    def __init__(self, nombre):    
        self.nombre = nombre
 
    def manejar(self):             
        raise NotImplementedError("la subclase debe implementar el metodo")
 
    def frenar(self):             
        raise NotImplementedError("la sublcase debe implementa el metodo")
 
class Deportivo(Automovil):
    def manejar(self):
        return 'Deportivo manejando en friega !'
 
    def frenar(self):
        return 'Deportivo frenando muy rapido!'
 
class Camioneta(Automovil):
    def manejar(self):
        return 'camioneta vendiendo '
 
    def frenar(self):
        return 'camioneta frenando para vender tamales!'
 
 
automoviles = [Camioneta('ford'),
        Camioneta('toyota'),
        Deportivo(' BMW Z6')]
 
for auto in automoviles:
    print(auto.nombre + ': ' + auto.manejar()+ " luego -->"+auto.frenar())