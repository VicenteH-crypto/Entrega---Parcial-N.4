
 # Definimos con def
def compra_entrada(usuarios):
    while True:
        if input('¿Desea comprar una entrada? (Si/No): ').strip().lower() != 'si':
            print('Hasta luego')
            return

        nombre = input('Ingrese su nombre: ').strip()
        nombre_clave = nombre.lower()

        tipo_entrada = input('Tipo de entrada ([1] Normal / [2] VIP): ').strip()

        while True:
            codigo = input('Cree un código de seguridad: ')
            if not codigo.strip() or ' ' in codigo:
                print('No puede dejar vacío ni usar espacios.')
                continue
            break

        usuarios[nombre_clave] = {
            'nombre': nombre,
            'tipo_entrada': tipo_entrada,
            'codigo_seguridad': codigo
        }
        print('Compra registrada.')

        if input('¿Continuar compando entradas? (si/no): ').strip().lower() != 's':
            print('Fin de compras.')
            return

def consultar_compradores(usuarios):
    buscar_comprador = input('Ingrese el nombre para buscar al comprador: ').strip().lower()

    if buscar_comprador in usuarios:
        u = usuarios[buscar_comprador]
        print('¡Si!, Usuario encontrado')
        print(f"Tipo de entrada: {u['tipo_entrada']}, Código de seguridad: {u['codigo_seguridad']}")
    else:
        print("No existe un comprador con ese nombre.")

def eliminar_usuario(usuarios):
    nombre_buscar = input('Ingrese el nombre del comprador que desea buscar: ').strip().lower()
    for i, (clave, u) in enumerate(list(usuarios.items())):
        if u['nombre'].strip().lower() == nombre_buscar:
            print(f"Comprador encontrado: {u['nombre']}")

            # Pregunta de confirmación
            respuesta = input("¿De verdad quieres eliminar a este usuario? "
                              "\nse eliminaran todos sus datos. \n(Si/No): ").strip().lower()
            if respuesta == 'si':
                usuarios.pop(clave)
                print("Usuario eliminado.")
            else:
                print("cancelando eliminación.")
            return
    print("No se encontró ningún comprador con ese nombre.")

# Mostramos las opciones a elegir usando main
def main():
    usuarios = {}
    while True:
        print(' ')
        print('Bienvenido a la boleteria.')
        print('1.- Comprar Entradas')
        print('2.- Consultar Comprador')
        print('3.- Eliminar un comprador')
        print('4.- Terminar la operación')
        print(' ')

        opcion = int(input('¿Que operación desea ejecutar?: '))

        if opcion == 1:
            compra_entrada(usuarios)
        elif opcion == 2:
            consultar_compradores(usuarios)
        elif opcion == 3:
            eliminar_usuario(usuarios)
        elif opcion == 4:
            print('¡Hasta luego!')
            break
        else:
            print('Esa opcion es invalida, intente nuevamente')

if __name__ == '__main__':
    main()