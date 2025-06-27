
 #ejercicio ingreso de usuario con def
def ingresar_usuario(usuarios):
    nombre = input("Nombre: ").strip()
    if nombre in usuarios:
        print("El nombre ya existe.")
        return

    sexo = input("Sexo (F/M): ").strip().upper()
    if sexo not in ("F", "M"):
        print("Sexo inválido.")
        return

    clave = input("Contraseña: ")
    if len(clave) < 8:
        print("Clave demasiado corta.")
    tiene_num = False
    tiene_letra = False
    for ch in clave:
        if ch.isdigit():
            tiene_num = True
        if ch.isalpha():
            tiene_letra = True
    if not (tiene_num and tiene_letra):
        print("Clave debe tener al menos una letra y un número.")
    usuarios[nombre] = {"sexo": sexo, "clave": clave}
    print("Ingreso Exitoso")

def buscar_usuario(usuarios):
    nombre = input("Nombre a buscar: ")

    if nombre in usuarios:
        u = usuarios[nombre]
        print(f"Sexo: {u['sexo']}, Clave: {u['clave']}")

    else:
        print("El usuario no se encuentra registrado")

def eliminar_usuario(usuarios):
    nombre = input("Nombre a eliminar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado")

    else:
        print("No existe ese usuario")

def main():
    usuarios = {}
    while True:
        print("\nsea bienvenido a mi menú, eliga la opción que desea operar:")
        print("1.- Ingresar usuarios")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Continuar o salir")
        opc = input("Ingrese opción (1-4): ")

        if opc == "1":
            ingresar_usuario(usuarios)
        elif opc == "2":
            buscar_usuario(usuarios)
        elif opc == "3":
            eliminar_usuario(usuarios)
        elif opc == "4":
            seguir = input("¿Continuar? (Si/No): ").strip().upper()
            if seguir == "No":
                print("Fin del programa.")
                break
        else:
            print("Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()