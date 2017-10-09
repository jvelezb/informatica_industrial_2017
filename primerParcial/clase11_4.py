import os
if not os.path.exists("/Users/juanvelezballesteros/repos/temporal_industrial/"):
	os.remove("/Users/juanvelezballesteros/repos/temporal_industrial/")
	os.makedirs("/Users/juanvelezballesteros/repos/temporal_industrial/")
archivo = open("/Users/juanvelezballesteros/repos/temporal_industrial/archivo4.txt","w+")
archivo.write("mario si va estudiar")
archivo.close()