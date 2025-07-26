def ingreso_cliente():
    clientes = {}
    try:
        cant_cliente = int(input("¿Cuántos clientes desea registrar? "))
        for i in range(cant_cliente):
            print(f"\nIngresando cliente #{i + 1}")
            while True:
                codigo = input("Ingrese el código del cliente: ").strip()
                if codigo in clientes:
                    print("Ese código ya existe. Intente con otro.")
                else:
                    break
            nombre = input("Ingrese el nombre del cliente: ")
            destinos = [] #lista para almacenar los destinos de cada cliente
            while True:
                try:
                    cant_destinos = int(input("Cuántos destinos quiere visitar (1-5): "))
                    if 1 <= cant_destinos <= 5:
                        break
                    else:
                        print("Debe ingresar un número en el rango (1-5)")
                except ValueError:
                    print("Ingrese un número entero")
            for j in range(cant_destinos):
                destino = input(f" Ingrese el destino No. {j+1}: ").strip()
                destinos.append(destino)
            clientes[codigo] = {"nombre": nombre, "destinos": destinos}
        return clientes
    except ValueError:
        print("Información inválida. Intente de nuevo.")

def mostrar_clientes(clientes):
    if not clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\nLista de clientes y destinos:")
        for codigo, datos in clientes.items():
            nombre = datos["nombre"]
            destinos = ', '.join(datos["destinos"])
            print(f"- Código: {codigo}, Nombre: {nombre}, Destinos: {destinos}")

def contar_destinos(clientes):
    codigos=list(clientes.keys())
    return cantidad_destinos(clientes,codigos)

def cantidad_destinos(clientes,codigos):
    if not codigos:
        return 0
    codigo_actual=codigos[0]
    destinos_actuales=len(clientes[codigo_actual]["destinos"])
    return destinos_actuales+cantidad_destinos(clientes,codigos[1:])

def menu():
    clientes = {}
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar clientes")
        print("2. Mostrar clientes y destinos")
        print("3. Mostrar total de destinos registrados")
        print("4. Salir")

        opcion = input("Ingrese una opcion: ").strip()

        if opcion=="1":
            nuevos=ingreso_cliente()
            clientes.update(nuevos)
        elif opcion=="2":
            mostrar_clientes(clientes)
        elif opcion=="3":
            total=contar_destinos(clientes)
            print(f"\nTotal de destinos: {total}")
        elif opcion=="4":
            print("Programa finalizado...")
            break
        else:
            print("Opcion invalida, elija otra opcion")
menu()
