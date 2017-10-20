import sys
sys.path.append("../")
from appJar import gui

def accion(boton):
	print(boton)


app=gui("calificacion","600x500")
app.setFont(20)

app.addLabelEntry("Matricula")
app.addLabelEntry("calificacion 1P")
app.addLabelEntry("calificacion 2P")
app.addLabelEntry("calificacion proyect")


app.setEntryDefault("calificacion 1P", "100")


app.addButtons(["Guardar","Generar Archivo"],accion)

app.go()