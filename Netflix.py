
 # Ejercicio Netflix
def anadir_contenido(miembro_netflix):
    nombre_usuario = input('Ingrese su nombre de usuario: ').strip()
    eleccion_entretenimiento = input('¿Que desea elegir'
                                     '\n1.- Peliculas '
                                     '\n2.- Series '
                                     '\nEscriba la opción: ')

    if eleccion_entretenimiento == 'Peliculas'.lower().strip():
        print('Selecciono peliculas')
        seleccion_categoria = int(input('Seleccione la categoria de su preferencia'
                                        '\n1.- Acción\n2.-Ciencia ficción\n3.- Terror\n4.- Comedia'
                                        '\nDigite la opción: '))

        miembro_netflix[nombre_usuario] = {
            'Nombre': nombre_usuario,
            'Formato': eleccion_entretenimiento,
            'Categoría': seleccion_categoria
        }
        print(' ')
        print(f'Selección de {eleccion_entretenimiento} exitosa para {nombre_usuario}.')
        return

    elif eleccion_entretenimiento == 'Series'.lower().strip():
        print('Selecciono Series')
        categoria_serie = int(input('Seleccion la categoria favorita'
                                    '\n1.- Acción\n2.-Ciencia ficción\n3.- Terror\n4.- Comedia'
                                    '\nDigite la opción: '))

        miembro_netflix[nombre_usuario] = {
            'Nombre': nombre_usuario,
            'Formato': eleccion_entretenimiento,
            'Categoria': categoria_serie
        }
        print(' ')
        print(f'Selección de {eleccion_entretenimiento} exitosa para {nombre_usuario}.')
        return
    else:
        print('Error.')

def mostrar_listado(miembro_netflix):
    opcion_mostrado = input(
        'Primero elige el formato:\n'
        'Películas\n'
        'Series\n'
        'Seleccione una opción: '
    ).strip().lower()

    if opcion_mostrado == 'películas' or opcion_mostrado == 'peliculas':
        print('Las películas disponibles son:\n'
              'a) Don’t Move\n'
              'b) Rescate Imposible\n'
              'c) Avatar\n'
              'd) Virgen a los 40')
    elif opcion_mostrado == 'series':
        print('Las series disponibles son:\n'
              'a) Stranger Things\n'
              'b) Avatar: La leyenda de Aang\n'
              'c) The Walking Dead\n'
              'd) BoJack Horseman')
    else:
        print('Opción inválida. Por favor escribe "Películas" o "Series".')

def anadir_tiempo(miembro_netflix):
    tipo = input('¿Desea ajustar el tiempo en películas o series?: ').lower().strip()
    if tipo == 'peliculas':
        print('Ha elegido películas. Opciones:')
        while True:
            try:
                opt = int(input(
                    'Seleccione una opción:\n'
                    '1) Cortas (≤40 min)\n'
                    '2) Medias (~1h y 30min)\n'
                    '3) Largas (≥2h)\n'
                    'Digite la opción: '
                ))
                if opt == 1:
                    print('Duración: cortas (≤40min).')
                    return
                elif opt == 2:
                    print('Duración: medias (~1h y 30min).')
                    return
                elif opt == 3:
                    print('Duración: largas (≥2h).')
                    return
                else:
                    print('Error: elija 1, 2 o 3.')
            except ValueError:
                print('Error: ingrese un número entero válido.')
    elif tipo == 'series':
        print('Ha elegido series. Opciones:')
        while True:
            try:
                opt = int(input(
                    'Seleccione una opción:\n'
                    '1) Cortas (<22min)\n'
                    '2) Medias (30–35min)\n'
                    '3) Largas (≥60min)\n'
                    'Digite la opción: '
                ))
                if opt == 1:
                    print('Duración: cortas (<22min).')
                    return
                elif opt == 2:
                    print('Duración: medias (30–35min).')
                    return
                elif opt == 3:
                    print('Duración: largas (≥60min).')
                    return
                else:
                    print('Error: elija 1, 2 o 3.')
            except ValueError:
                print('Error: ingrese un número entero válido.')
    else:
        print('Opción no válida. Por favor escriba "peliculas" o "series".')

def main():
    miembro_netflix = {}
    while True:
        print(' ')
        print('Bienvenido a nuestra plataforma de entretenimiento "Netflix".')
        print('1.- Añadir peliculas o series.')
        print('2.- mostrar listado de peliculas o series.')
        print('3.- Añadir tiempo de la pelicula/Serie.')
        print('4.-Terminar programa.')

        opcion_menu = int(input('Seleccione el número de la operación, que quiere que se ejecute: '))
        if opcion_menu == 1:
            anadir_contenido(miembro_netflix)
        elif opcion_menu == 2:
            mostrar_listado(miembro_netflix)
        elif opcion_menu == 3:
            anadir_tiempo(miembro_netflix)
        elif opcion_menu == 4:
            salir = input('¿Desea terminar programa? (si/no): ')
            if salir != 'no':
                print('Hasta luego...')
                break
        else:
            print('ERROR... Vuelva ha seleccionar una opción valida.')

if __name__ == '__main__':
   main()