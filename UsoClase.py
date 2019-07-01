class Estudiante(object):
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

 
    def hola(self):
        return 'Mi nombre es %s y tengo %i' % (self.nombre,self.edad)

e=Estudiante ("Robert",35)
s=e.hola()
print(s)