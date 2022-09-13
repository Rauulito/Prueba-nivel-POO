
from Coche import Coche

#creamos la clase camioneta
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga): #Se heredan los atributos de la clase coche y definimos los adicionales de la clase camioneta
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self): #preparamos el formato de salida
        return Coche.__str__(self) + " {} kg".format(self.carga)

#prueba
if __name__== '__main__':
    c = Camioneta("azul", 4, 150, 1200,500)
    print(type(c).__name__,":",c)