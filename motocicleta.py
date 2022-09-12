from vehiculo import vehiculo
class motocicleta(vehiculo):
    def __init__(self, color, ruedas,tipo, velocidad, cilindrada):
        vehiculo.__init__(self, color, ruedas)
        self.tipo=tipo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return vehiculo.__str__(self) + ", {}, {} km/h, {}cc".format(self.tipo,self.velocidad, self.cilindrada)

#prueba
c = motocicleta("verde", 2,"urbana", 120, 1100)
print(c)