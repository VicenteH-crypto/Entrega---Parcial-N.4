
 # Ejercicio de GitHub
def vender_entradas():
    respuesta = input("¿Quieres comprar entradas? (Si/No): ").strip().lower()
    if respuesta != 'si':
        print("Pierdase >:v.")
        return

    print("Shows:")
    print("1) Maniobras")
    print("2) Sonrisa")
    show = input("Selecciona 1 o 2: ").strip()

    if show == '1':
        stock_file = "Entradas_Maniobras.txt"
    else:
        stock_file = "Entradas_Maniobras.txt"

    f = open(stock_file, "r")
    stock = int(f.readline())
    f.close()
    print("Quedan", stock, "entradas")

    cantidad = int(input("¿Cuántas quieres?: "))
    if cantidad <= stock:
        stock -= cantidad
        f = open(stock_file, "w")
        f.write(str(stock))
        f.close()
        print("Compra registrada!")
    else:
        print("No hay suficientes entradas.")

def cambiar_show():
    cambio = input("¿Quieres cambiar de show? (Si/No): ").strip().lower()
    if cambio == 'si':
        nuevo = input("Elegir nuevo show (1 o 2): ").strip()
        if nuevo == '1':
            print("Cambiado a Maniobras.")
        elif nuevo == '2':
            print("Cambiado a Sonrisa.")
        else:
            print("Show no válido.")
    else:
        print("No cambiaste de show.")

def ver_stock():
    show = input("¿Qué show? (1=Maniobras, 2=Sonrisa): ").strip()
    if show == '1':
        archivo = "Entradas_Maniobras.txt"
    elif show == '2':
        archivo = "Entradas_Sonrisa_Iluminada.txt"
    else:
        archivo = "Entradas_Maniobras.txt"

    f = open(archivo, "r")
    stk = f.readline()
    f.close()
    print("Quedan", stk, "entradas")

def main():
    while True:
        print("\nTeatro GitHub")
        print("1) Vender entradas")
        print("2) Cambiar show")
        print("3) Ver stock")
        print("4) Salir")
        opcion = input("Elige una opción (1–4): ").strip()

        if opcion == '1':
            vender_entradas()
        elif opcion == '2':
            cambiar_show()
        elif opcion == '3':
            ver_stock()
        elif opcion == '4':
            salir = input("¿Salir? (Si/No): ").strip().lower()
            if salir == 'si':
                print("Adiós!")
                break
            else:
                print("Regresando al menú...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()