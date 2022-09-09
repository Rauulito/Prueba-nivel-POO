
class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    #utilizamos para coche y bicicleta
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
