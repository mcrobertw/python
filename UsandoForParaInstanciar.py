class Estudiante(object):
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

 
    def hola(self):
        return 'Mi nombre es %s y tengo %i' % (self.nombre,self.edad)

lista_de_alumnos = list()
for contador in range(10):
	nombre = "Estudiante %i" % contador
	e=Estudiante(nombre,contador+10)
	lista_de_alumnos.append(e)

#print (lista_de_alumnos)#Imprime la dirección de memoria de los objetos

for est in lista_de_alumnos:
		print ("Estudiante: %s " %est.nombre, "Edad: %i" %est.edad)

