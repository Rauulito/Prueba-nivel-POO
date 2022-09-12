from vehiculo import vehiculo

#creamos la clase camioneta
class camioneta(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga=carga

    def __str__(self):
        return vehiculo.__str__(self) + ", {} km/h, {}cc,{} kg".format(self.velocidad, self.cilindrada,self.carga)

#prueba
c = camioneta("azul", 4, 150, 1200,500)
print(c)