from appJar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Nombre")
        pwd = app.getEntry("Contraseña")
        print("User:", usr, "Pass:", pwd)

# create a GUI variable called app
app = gui("Hola a todos", "600x500")
app.setBg("red")
app.setFont(40)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Informatica industrial")
app.setLabelBg("title", "orange")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Nombre")
app.addLabelSecretEntry("Contraseña")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Nombre")

# start the GUI
app.go()