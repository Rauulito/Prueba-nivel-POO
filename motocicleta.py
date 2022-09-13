from Bicicleta import Bicicleta
#creamos la clase Motocicleta
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada): #Se heredan los atributos de la clase Bicleta y definimos los adicionales de la clase Motocicleta
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self): #preparamos el formato de salida
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

#prueba
if __name__== '__main__':
    c = Motocicleta("verde", 2,"urbana", 120, 1100)
    print(type(c).__name__,":",c)