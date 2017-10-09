import math
def volumen_esfera(radio):
	volumen = math.pi*4*radio**3/3
	return volumen

def main():
	radio = 3
	vol = volumen_esfera(radio)
	print(vol)

main()