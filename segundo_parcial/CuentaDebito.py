from Cuenta import Cuenta

class CuentaDebito(Cuenta):

	def __init__(self, saldoInicial, nombre):
		if saldoInicial > 0:
			Cuenta.__init__(self, nombre)
			self.saldo = saldoInicial
	
	def hacerDeposito(self, monto):
		self.saldo += monto
		
	def hacerRetiro(self, monto):
		if monto <=self.saldo:
			self.saldo -= monto
		else:
			print("no tienes esa lana, saca menos dinero")


# cuenta = CuentaDebito(100)
# cuenta.hacerDeposito(50)
# print("El saldo es: ", cuenta.obtenerSaldo())
# cuenta.hacerRetiro(60)
# print("El saldo es: ", cuenta.obtenerSaldo())
# cuenta.hacerRetiro(360)
# print("El saldo es: ", cuenta.obtenerSaldo())

		

