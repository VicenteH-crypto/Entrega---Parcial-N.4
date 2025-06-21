
import time
aStock = 0

 # Imprimimos datos
print(' ')
print('Bienvenido al CinePlanet del Mall florida center')
print('_________________________________________________')
print(' ')

 # Confirmacion & condincional
respuesta_cine = input('¿Desea comprar entradas al cine? (Si/No): ')

if respuesta_cine == 'si'.lower():
    time.sleep(4.5)
    print('1.- Star Wars III - la venganza de los sith')
    print('2.- Cómo entrenar a tu dragón')
    print('3.- Misión imposible: sentencia final')
    print('4.- Alien - el octavo pasajero')
    print(' ')

    time.sleep(3)
    print('¿Entradas para que pelicula?')
    time.sleep(2)
    print(' ')

    aPelicula = input('Ingrese el nombre de la pelicula tal cual aparece: ')

    match aPelicula.upper():
        case "STAR WARS III - LA VENGANZA DE LOS SITH":
            afile = open('Entradas_StarWars2005.txt', 'r')
            aStock = afile.readline()
            print('Queda', aStock, 'entradas')
            afile.close()
        case "COMO ENTRENAR A TU DRAGON":
            afile = open('Entradas_dragones.txt', 'r')
            aStock = afile.readline()
            print('Queda', aStock, 'entradas')
            afile.close()
        case "MISION IMPOSIBLE: SENTENCIA FINAL":
            afile = open('Entradas_Mision imposible.txt', 'r')
            aStock = afile.readline()
            print('Queda', aStock, 'entradas')
            afile.close()
        case "ALIEN - EL OCTAVO PASAJERO":
            afile = open('Entradas_Alien-8 passenger.txt', 'r')
            aStock = afile.readline()
            print('Queda', aStock, 'entradas')
            afile.close()

    # Ahora la parte de ingresar la cantidad de entradas que se compraran
    print(' ')
    time.sleep(1.5)
    aCantidad_entradas = input('¿Cuantas entradas desea comprar?: ')
    aStock = int(aStock) - int(aCantidad_entradas)
    match aPelicula.upper():
        case "STAR WARS III - LA VENGANZA DE LOS SITH":
            afile = open('Entradas_StarWars2005.txt', 'w+')
            afile.write(str(aStock))
        case "COMO ENTRENAR A TU DRAGON":
            afile = open('Entradas_dragones.txt', 'w+')
            afile.write(str(aStock))
        case "MISION IMPOSIBLE: SENTENCIA FINAL":
            afile = open('Entradas_Mision imposible.txt', 'w+')
            afile.write(str(aStock))
        case "ALIEN - EL OCTAVO PASAJERO":
            afile = open('Entradas_Alien-8 passenger.txt', 'w+')
            afile.write(str(aStock))

    print(' ')
    time.sleep(3)
    print('Que disfrute la pelicula')
    
else:
    print('Chao pescado.....')