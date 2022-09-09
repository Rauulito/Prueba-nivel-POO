from vehiculo import vehiculo
class motocicleta(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

#prueba
c = motocicleta("verde", 2, 120, 1100)
print(c)