from vehiculo import vehiculo

class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        vehiculo.__init__(self, color, ruedas)
        self.carga = tipo


    def __str__(self):
        return vehiculo.__str__(self) + ", {} ".format(self.tipo)

#prueba
c = bicicleta("verde", 4, "urbana")
print(c)