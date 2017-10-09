import math

def perimetro_circulo(radio):
	perimetro = math.pi * 2 * radio
	return perimetro



def informacion_circulo(radio):
	print("circulo string")
	perimetro = math.pi *2 *float(radio)
	area = math.pi * float(radio) ** 2
	return perimetro , area

def informacion_circulo(radio,color):
	print("circulo float")
	def area(radio):
		return math.pi * radio ** 2
	def perimetro(radio):
		return math.pi *2 *radio

	perimetro = perimetro(radio)
	area = area(radio)
	return perimetro , area

def main():
	#radio = input('Dame el radio')
	print("El tipo es:",type(radio))
	##resultado = perimetro_circulo(radio)
	##print("El perimetro es: ", resultado)
	perimetro, area = informacion_circulo(float(radio),color)
	##perimetro2, area2 = informacion_circulo(float(radio))
	print("el perimetro es:",perimetro)
	print("El area es: ", area)

radio = 32.3
color = "rojo"
main()









