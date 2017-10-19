from abc import ABC, abstractmethod
from Cliente import Cliente

class Cuenta(ABC):

	def __init__(self,nombre):
		self.saldo = 0 
		self.cliente = Cliente(nombre)

	@abstractmethod
	def hacerDeposito(self, monto):
		pass


	@abstractmethod
	def hacerRetiro(self, monto):
		pass

	def obtenerSaldo(self):
		return self.saldo