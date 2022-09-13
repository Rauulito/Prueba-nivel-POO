from Vehiculo import Vehiculo

#creamos la clase bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):  #Se heredan los atributos de la clase vehiculo y definimos los adicionales de la clase bicicleta
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo


    def __str__(self): #preparamos el formato de salida
        return Vehiculo.__str__(self) + ", {} ".format(self.tipo)

#prueba
if __name__== '__main__':
    c = Bicicleta("verde", 2, "urbana")
    print(type(c).__name__,":",c)