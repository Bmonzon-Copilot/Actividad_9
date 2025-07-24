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
            destinos = []
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

print(ingreso_cliente())

