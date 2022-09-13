#Importamos todas las clases que vamos a utilizar
from Vehiculo import Vehiculo
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta

#creamos la funcion catalogar
def catalogar(lista):
    for elemento in lista: #recorremos toda la lista, mostrando para cada elemento el nombre de su clase y sus atributos
        print(type(elemento).__name__,":",elemento)

if __name__== '__main__':
    #Creamos un objeto de casa subclase
    co = Coche("azul", 4, 150, 1200)
    ca = Camioneta("verde", 6, 120, 3000,5000)
    bi = Bicicleta("negro", 2, "urbana")
    mo = Motocicleta("blanca", 2,"deportiva", 200, 1000)

    #creamos una lista y añadimos los vehiculos que hemos  creado
    Vehiculos=[]
    Vehiculos.append(co)
    Vehiculos.append(ca)
    Vehiculos.append(bi)
    Vehiculos.append(mo)

    #llamamos a la funcion catalogar
    catalogar(Vehiculos)