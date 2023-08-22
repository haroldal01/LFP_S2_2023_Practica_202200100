elementos = {}
finales = {}

def cargar_inicial(inicial):
    with open(inicial, encoding="utf-8") as file:
        for fila in file:
            producto, cantidad, precio, ubicacion = fila.strip().split(" ")[1].split(";")

            if ubicacion in elementos:
                elementos[ubicacion][producto] = {
                    "cantidad": float(cantidad),
                    "precio": float(precio)
                }
            else:
                elementos[ubicacion] = {
                    producto: {
                    "cantidad": float(cantidad),
                    "precio": float(precio)}

                }
    #print(elementos)

def cargar_movimientos(movimientos):
    with open(movimientos, encoding="utf-8") as file:
        for fila in file:
            instruccion, informacion = fila.strip().split(" ")
            producto, cantidad, ubicacion = informacion.split(";")

            if instruccion == "agregar_stock":
                if ubicacion not in elementos:
                    print(ubicacion, "no está disponible en las ubicaciones")

                    continue
                if producto not in elementos[ubicacion]:
                    print(producto, " no está disponible en ", ubicacion)
                    continue

                cantidad_final = float(elementos[ubicacion][producto]["cantidad"])
                cantidad_final += float(cantidad)

    
                elementos[ubicacion][producto]["cantidad"] = cantidad_final
                

            elif instruccion == "vender_producto":
                if ubicacion not in elementos:
                    print(ubicacion, "no está disponible en las ubicaciones")

                    continue
                if producto not in elementos[ubicacion]:
                    print(producto, " no está disponible en ",ubicacion)
                    continue

                cantidad_final = float(elementos[ubicacion][producto]["cantidad"])
                
                cantidad_final -= float(cantidad)

             

                if cantidad_final < 0:
                    print("no se pueden vender más ", producto, " de los que hay disponibles")

                else:
                    elementos[ubicacion][producto]["cantidad"] = cantidad_final

            else:
                print("Instrucción no válida")

    finales.update(elementos)

   


def generar_archivo():
    with open("C:\\Users\\81vv00k9gj\\OneDrive\\Escritorio\\universidad\\lfp\\practica1LFP\\informe_final.txt", "w", encoding="utf-8") as file:
        file.write("Informe de Inventario:\n")
        file.write("{:<15} {:<10} {:<15} {:<15} {:<15}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"))
        file.write("-" * 70 + "\n")
        
        for ubicacion, productos in finales.items():
            for producto, valores in productos.items():
                cantidad = valores["cantidad"]
                precio_unitario = valores["precio"]
                valor_total = cantidad * precio_unitario
                
                file.write("{:<15} {:<10} {:<15} {:<15} {:<15}\n".format(producto, cantidad, "Q" + str(precio_unitario), "Q" + str(valor_total), ubicacion))






opcion = 0
contador_inicial = 0


while opcion != 4:
    print("1) Cargar inventario inicial\n2) Cargar instrucciones de movimientos\n3) Crear informe de movimiento\n4) Salir")

    opcion = int(input())

    if opcion == 1:
        print("ingrese la ruta del inventario inicial")
        inven_inicial = input()
        cargar_inicial(inven_inicial)
        contador_inicial += 1
        print("se ha cardado el archivo")

    elif opcion == 2:
        print("")
        if contador_inicial > 0:
            ruta_movimientos = input(" ingrese la ruta del archivo ")
            cargar_movimientos(ruta_movimientos)
        else:
            print("no se ha cargado el inventario inicial")

    elif opcion == 3:
        print("Crear informe de movimientos")
        if contador_inicial > 0:
            generar_archivo()
            print("Informe de movimientos creado.")
        else:
            print("No se ha cargado ningún archivo")

    elif opcion == 4:
        print("Saliendo...")
        break

    else:
        print("ingrese una opción válida")



