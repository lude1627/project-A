carrito = {}

print("🛒 ¡Bienvenido al Carrito de Compras!")

while True:
    print("\nSeleccione una opción:")
    print("1. Añadir artículo")
    print("2. Ver carrito")
    print("3. Eliminar artículo")
    print("4. Calcular total")
    print("5. Salir")

    try:
        opcion = int(input("👉 Escriba el número de la opción: "))
    except ValueError:
        print("⚠️ Por favor, escriba un número válido.")
        continue

    if opcion == 1:
        articulo = input("🔹 ¿Qué artículo desea añadir? ")
        try:
            precio = float(input("💲 Ingrese el precio: "))
            carrito[articulo] = precio
            print(f"✅ '{articulo}' se agregó al carrito por ${precio:.0f}")
        except ValueError:
            print("⚠️ El precio debe ser un número.")

    elif opcion == 2:
        if carrito:
            print("\n🛍️ Su carrito contiene:")
            for articulo, precio in carrito.items():
                print(f"   - {articulo}: ${precio:.0f}")
        else:
            print("📭 El carrito está vacío.")

    elif opcion == 3:
        if carrito:
            eliminar = input("❌ ¿Qué artículo desea eliminar? ")
            if eliminar in carrito:
                carrito.pop(eliminar)
                print(f"✅ '{eliminar}' fue eliminado del carrito.")
            else:
                print("⚠️ Ese artículo no está en el carrito.")
        else:
            print("📭 El carrito está vacío.")

    elif opcion == 4:
        if carrito:
            total = sum(carrito.values())
            print(f"💵 El total de su compra es: ${total:.2f}")
        else:
            print("📭 El carrito está vacío.")

    elif opcion == 5:
        print("👋 Gracias por usar el carrito. ¡Vuelva pronto!")
        break

    else:
        print("⚠️ Opción no válida, intente de nuevo.")
