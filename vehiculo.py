

#creamos la clase vehiculo
class Vehiculo():
    def __init__(self, color, ruedas): #definimos los atributos de la clase Vehiculo
        self.color = color
        self.ruedas = ruedas

    def __str__(self): #preparamos el formato de salida
        return "color {}, {} ruedas".format( self.color, self.ruedas )

#prueba
if __name__== '__main__':
    c = Vehiculo("azul", 4)
    print(type(c).__name__,":",c)