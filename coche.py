from Vehiculo import Vehiculo
#creamos la clase coche
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada): #Se heredan los atributos de la clase vehiculo y definimos los adicionales de la clase coche
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self): #preparamos el formato de salida
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

#prueba
if __name__== '__main__':
    c = Coche("azul", 4, 150, 1200)
    print(type(c).__name__,":",c)
