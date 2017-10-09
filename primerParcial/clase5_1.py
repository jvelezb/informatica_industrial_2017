matrix = [[12,12,23,34.3,34,34,],[23,34,45,23],[23,23,45,23],[23,54,12,23],[]]
print(matrix[0]) #[12,12,23,34]
print(matrix[0][3])
print(matrix[len(matrix)-1])
for m2 in matrix:
	try:
		print ("lo encontre: ",m2.index(34.3))
		break
	except:
		print("no se encontro en",m2)
		m2.append(34.4)
		print("nueva lista",m2)
print(matrix)
