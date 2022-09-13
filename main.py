#Importamos todas las clases que vamos a utilizar
from Vehiculo import Vehiculo
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta

#creamos la funcion catalogar
def catalogar(lista,numero=-1): #ponemos -1 como valor del parametro opcional para saber si nos lo pasan
    if numero >= 0: #Si se pasa el parametro opcional de numero de ruedas
        total=0 #Creamos una variable para contar cuantos vehiculos tienen el numero de ruedas que se pase
        for elemento in lista: #recorremos toda la lista
            if elemento.ruedas==numero: #Si coincicde el numero de ruedas se imprime el elemento y se suma 1 al contador
                print(type(elemento).__name__,":",elemento)
                total=total+1
        print("Se han encontrado {} vehículos con {} ruedas".format(total,numero)) #Se imprime el total de vehiculos encontrados
    else: #Si no se pasa el parametro opcional
        for elemento in lista: #recorremos toda la lista, mostrando para cada elemento el nombre de su clase y sus atributos
            print(type(elemento).__name__,":",elemento)

if __name__== '__main__':
    #Creamos un objeto de casa subclase
    co = Coche("azul", 4, 150, 1200)
    ca = Camioneta("verde", 4, 120, 3000,5000)
    bi = Bicicleta("negro", 2, "urbana")
    mo = Motocicleta("blanca", 2,"deportiva", 200, 1000)

    #creamos una lista y añadimos los vehiculos que hemos  creado
    Vehiculos=[]
    Vehiculos.append(co)
    Vehiculos.append(ca)
    Vehiculos.append(bi)
    Vehiculos.append(mo)

    #llamamos a la funcion catalogar sin el parametro opcional
    catalogar(Vehiculos)

    #llamamos a la funcion catalogar con el parametro opcional
    catalogar(Vehiculos, 0)
    catalogar(Vehiculos, 2)
    catalogar(Vehiculos, 4)