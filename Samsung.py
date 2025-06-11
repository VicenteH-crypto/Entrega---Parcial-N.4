
 # Ejercicio Directorio Samsung

 # Crear una diccionario vacía
contacto = {}

 # creo diccionario con los datos a pedir
contacto = {'Nombre': ' ', 'Apellido': ' ', 'Dirección': ' ', 'Edad': ' ', 'Nota': ' '}

 # Damos la bienvenida
print('Hola, para agregar un contacto al directorio deberá ingresar los siguientes datos:')
print(' ')

 # Requisitos
print('1.- Nombre')
print('2.- Apellido')
print('3.- La dirección')
print('4.- Edad')
print('5.- y la nota (Maximo 50 letras)')
print('-----------------------------------------')
print(' ')

 # escribimos los datos
nombre_contacto = input('Ingrese el nombre de usuario: ')
contacto['Nombre'] = nombre_contacto

surname_contacto = input('Ingrese el apellido: ')
contacto['Apellido'] = surname_contacto

direccion_contacto = input('Ingrese la dirección de casa: ')
contacto['Dirección'] = direccion_contacto

while True:
    try:
        edad_contacto = int(input('Ingrese la edad actual: '))
        if edad_contacto <= 100 and edad_contacto > 0:
            contacto['Edad'] = edad_contacto
            break
        else:
            print('Edad invalida, intenta nuevamente')
    except ValueError:
        print('ERROR... el número debe ser ENTERO válido.')

while True:
    Nota = input('Ingrese una nota (Máximo 50 caracteres): ')
    if len(Nota) <= 50:
        contacto['Nota'] = Nota
        break
    else:
        print('No puede excederce de 50 caracteres. Inténtelo denuevo.')

 # Guardamos la información que tenemos
with open('Directorio_contactos.txt', 'w+') as archivo:
    archivo.write(f'Nombre: {contacto['Nombre']}\n')
    archivo.write(f'Apellido: {contacto['Apellido']}\n')
    archivo.write(f'Dirección: {contacto['Dirección']}\n')
    archivo.write(f'Edad: {contacto['Edad']}\n')
    archivo.write(f'Nota: {contacto['Nota']}\n')
    archivo.write('\n')

print('\nContacto ingresado')
print(contacto)