from Cuenta import Cuenta

class CuentaCredito(Cuenta):

	def __init__(self, limiteCredito,nombreCliente):
			Cuenta.__init__(self,nombreCliente)
			self.limiteCredito = limiteCredito
	
	def hacerDeposito(self, monto):
		self.saldo += monto
		
	def hacerRetiro(self, monto):
		if (self.saldo + monto) < self.limiteCredito:
			self.saldo-= monto
		else:
			print("vas a exceder tu limite de credito que es: ",self.limiteCredito)



credito = CuentaCredito(100,"Juan")
credito.hacerDeposito(10)
print("El saldo de la tarjeta es:",credito.obtenerSaldo())
credito.hacerRetiro(100)
print("El saldo de la tarjetaes:",credito.obtenerSaldo())
credito.hacerRetiro(200)
print("El saldo de la tarjetaes:",credito.obtenerSaldo())
print("El nombre del cliente propietario de la cuenta es: ",credito.cliente.nombre)

