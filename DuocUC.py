
 # Ejercicios Alumnos_DuocUC
datos_guardados = []

 # Damos la bienvenida
print(' ')
print('Bienvenido a Duoc UC, usted almanacera sus datos personales.')
print(' ')

print('Los datos que debera registrar son:')
print('1.- Nombre.')
print('2.- Apellido.')
print('3.- r.u.t.')
print('4.- Correo electrónico.')
print('5.- Y la carrera')
print('----------------------------------------------------------------------------')
print(' ')

 # Pedimos los datos
alias_estudiantes = input('Ingrese su nombre: ')
datos_guardados.append(alias_estudiantes)

apellido_estudiantes = input('Ahora el apellido: ')
datos_guardados.append(apellido_estudiantes)

while True:
        rut = input('Ingrese el R.U.T (Sin puntos, ni guión): ')
        if len(rut) <= 9:
            datos_guardados.append(rut)
            break
        else:
            print('Incorrecto, solo está permitido 9 digitos, No más.')

Correo_electronico = input('Indique su correo electrónico del instituto: ')
datos_guardados.append(Correo_electronico)

carrera = input('Indique su carrera (Ingenieria, Analista o Gastronomia): ')
if carrera != 'Ingenieria' and carrera != 'Analista' and carrera != 'Gastronomia':
    print('incorrecto, usted tuvo que haber elegido una de las que estaba en la lista. Se asignará "Desconocida".')
    carrera = 'Desconocida'
datos_guardados.append(carrera)

 # guardamos la info en el archivo
with open('Estudiantes_DuocUc.txt', 'w+') as archive:
    archive.write(' / '.join(datos_guardados) + '\n')
print(' ')
print(datos_guardados)