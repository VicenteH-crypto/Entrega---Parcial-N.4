
#Ejercicio del Hospital central santiago

def hora_paciente(paciente):
    confirmacion_veredicto = input('¿Desea pedir una hora al Hospital Central de Santiago? (Si/No): ').strip().lower()

    if confirmacion_veredicto == 'si':
        nombre_paciente = input('Ingrese el nombre y apellido del paciente: ').strip()

        try:
            numero_rut = int(input('Ingrese su RUT, sin puntos, ni guion, y sin dígito verificador: ').strip())
        except ValueError:
            print('Error: debe ingresar solo números.')
            return
        if numero_rut < 1 or numero_rut > 99_999_999:
            print('Error... no puede exceder 8 dígitos ni ser menor que 1.')
            return
        else:
            print('R.U.T registrado exitosamente.')

        try:
            enfermedades = int(input(
                'Seleccione el tipo de enfermedad que padece\n'
                '1.- Heridas punzo-penetrantes\n'
                '2.- Virus\n'
                '3.- Hemorragias\n'
                '4.- Reacciones alérgicas\n'
                '5.- Deshidratación crónica\n'
                '6.- Otras\n'
                'Digite la opción: '
            ).strip())
        except ValueError:
            print('Error: seleccione una opción numérica válida.')
            return

        if enfermedades == 1:
            print('Ha indicado "Heridas punzo-penetrantes".')
        elif enfermedades == 2:
            print('Ha indicado "Virus".')
        elif enfermedades == 3:
            print('Ha indicado "Hemorragias".')
        elif enfermedades == 4:
            print('Ha indicado "Reacciones alérgicas".')
        elif enfermedades == 5:
            print('Ha indicado "Deshidratación crónica".')
        elif enfermedades == 6:
            print('Ha indicado "Otras enfermedades".')
        else:
            print('Opción inválida, seleccione nuevamente.')
            return

        comuna_direccion = input('Por último ingrese la comuna en donde vive y la dirección (ej. Santiago Centro / Calle Falsa 123): ').strip().lower()

        if comuna_direccion.startswith('santiago centro'):
            print(f'La comuna "{comuna_direccion}" es donde estamos ubicados.')
        else:
            print('El paciente no pertenece a nuestra comuna.')

        paciente[nombre_paciente] = {
            'Nombre del paciente': nombre_paciente,
            'R.U.T': numero_rut,
            'Enfermedad': enfermedades,
            'Comuna y Dirección': comuna_direccion
        }
        print(' ')
        print('¡El paciente ha sido registrado!, pronto le daremos fecha y hora.')
        print(' ')
        return
    else:
        print('Regrese a casa...')
        return

def mostrar_pacientes(paciente):
    buscar_paciente = input('Ingrese el nombre y apellido para buscar al paciente: ')

    if buscar_paciente in paciente:
        print(' ')
        print(f'El usuario "{buscar_paciente}" ha sido encontrado')
        print(' ')
    else:
        print(' ')
        print('No existe un paciente con ese nombre y apellido')
        print(' ')


def eliminar_paciente(pacientes):
    respuesta = input('¿Desea eliminar a un paciente? (Si/No): ').strip().lower()
    if respuesta != 'si':
        print('Operación cancelada.')
        return

    try:
        rut_buscado = int(input('Ingrese el R.U.T (sin puntos ni dígito verificador): ').strip())
    except ValueError:
        print('Error: debe ingresar un número válido.')
        return

    for nombre, datos in list(pacientes.items()):
        if datos.get('R.U.T') == rut_buscado:
            print(f'Se ha encontrado al paciente "{nombre}": {datos}')
            confirm = input('¿Está seguro que desea eliminarlo? (Si/No): ').strip().lower()
            if confirm == 'si':
                pacientes.pop(nombre)
                print(' ')
                print(f'Paciente "{nombre}" eliminado.')
                print(' ')
            else:
                print(' ')
                print('Eliminación cancelada.')
                print(' ')
            return

    print(f'No se encontró ningún paciente con R.U.T {rut_buscado}.')

def main():
    paciente = {}
    while True:
        print('Bienvenido a la pagina web del hospital central de santiago')
        print('1.- Pedir hora para paciente.')
        print('2.- Buscar a paciente.')
        print('3.- Eliminar a un paciente')
        print('4.- Salir')

        opc = int(input('Selecione una opción: '))
        if opc == 1:
            hora_paciente(paciente)
        elif opc == 2:
            mostrar_pacientes(paciente)
        elif opc == 3:
            eliminar_paciente(paciente)
        elif opc == 4:
            salir_pagina = input('¿Desea salir de nuestra pagina? (Si/No): ')
            if salir_pagina != 'No'.lower().strip():
                print('Ha salido de nuestra pagina.')
                break
        else:
            print('Esa opción no existe...Intente nuevamente')

if __name__ == '__main__':
    main()