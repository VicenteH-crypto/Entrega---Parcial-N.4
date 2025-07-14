
 # ejercicio examen final
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
             }

stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
        'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
        'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
        }

def stock_marca(marca):
    stock = 0
    for modelo, in productos.items:
     if productos[modelo][0].lower() == marca[productos].lower():
        total += stock[modelo][1]
    print(f'El "Stock" total de la marca es de: {total}')
             
def busqueda_precio(p_min, p_max):
    busqueda = []
    for modelo in stock:
        precio, stock = productos[modelo]

    if p_min <= precio <= p_max and stock > 0:

        busqueda.append(f"{productos[modelo][0]}--{modelo}")
    else:
        print('El modelo ingresado no eixste... preube nuevamente.')

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        print('¡¡Precio actualizado!!.')
    else:
        print('El precio no fue actualizado.')

def main():
    while True:
        print(' ')
        print('bienvenido a Pybooks')
        print('_____________________')
        print('1.- Stock de marca.')
        print('2.- Búsqueda por precio')
        print('3.- Actualizar precio')
        print('4.- Salir')

        opc_final = int(input('Seleccione una opción: '))

        if opc_final == 1:
            marca = input('Ingrese el nombre del a marca: ')
            stock_marca(marca[productos])
        elif opc_final == 2:
            while True:
                try:
                    p_min = int(input('Ingrese el precio minimo: '))
                    p_max = int(input('Ahora, con precio maximo: '))
                    if p_min <= 0 and p_min >= p_max:
                        print('Error, el precio minimo no puede ser menor o igual a 0.')
                    else:
                        break
                except ValueError:
                    print('ERRROR... el numero ingresado no es un número ENTERO válido, intente nuevamente.')
            busqueda_precio(p_min, p_max)
        elif opc_final == 3:
            modelo_actualizar = input('Ingrese mdelo a actualizar: ')
            try:
                    p = int(input('Ingrese el nuevo precio: '))
                    if p <= 0:
                        print('Incorrecto. El precio no puede ser un número menor o igual a zero, intente nuevamente.')
                    else:
                        actualizar_precio(modelo_actualizar, p)
                    confirmacion = input('¿Desea actualizar otro precio? (Si/No): ')
                    if confirmacion == 'si':
                        print('hA INDICADA que bno')
                    else:
                        print('Repita el proceso')
                        modelo_actualizar = input('Ingrese mdelo a actualizar: ')
                        p = int(input('Ingrese el nuevo precio: '))
                        actualizar_precio(modelo_actualizar, p)
            except ValueError:
                    print('El valornuevo no puede estar en decimales.')

        elif opc_final == 4:
            salir = input('¿Desea salir del programa? (Si/No): ')
            if salir == 'Si'.lower:
                print('HASTA PRONTO')
                break
            else:
                print('Regrese a elegir.')

if __name__ == '__main__':
    main()