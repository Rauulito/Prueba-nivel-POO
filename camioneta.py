
from coche import coche

#creamos la clase camioneta
class camioneta(coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
        return coche.__str__(self) + " {} kg".format(self.carga)

#prueba
c = camioneta("azul", 4, 150, 1200,500)
print(c)