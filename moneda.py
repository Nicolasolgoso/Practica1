#Pedimos al usuario que ingrese la cantidad en euros a convertir
euros = float(input("Introduce la cantidad en euros que quieres convertir: "))
#Le preguntamos a que moneda pretende convertir los euros
cambio = int(input("Para convertirlo a: \n dólares marca 1: \n pesos marca 2: \n yuanes marca 3: \n libras marca 4: \n francos suizos marca 5: \n "))
#Si elige dolares realizamos la conversión a dólares
if cambio == 1:
    conversion_dolares = euros * 0.94
    print(f"Equivale a {conversion_dolares} dólares")
#Si elige pesos realizamos la conversión a pesos
elif cambio == 2:
    conversion_pesos = euros * 19.25
    print(f"Equivale a {conversion_pesos} pesos")
#Si elige yuanes realizamos la conversión a yuanes
elif cambio == 3:
    conversion_yuanes = euros * 7.63
    print(f"Equivale a {conversion_yuanes} yuanes")
#Si elige libras realizamos la conversión a libras
elif cambio == 4:
    conversion_libras = euros * 1.15
    print(f"Equivale a {conversion_libras} libras")
#Si elige francos realizamos la conversión a francos
elif cambio == 5:
    conversion_francos_suizos = euros * 0.96
    print(f"Equivale a {conversion_francos_suizos} francos suizos")
#Si introduce algo distinto de un número de el 1 al 5 da error
else:
    print("Error.Por favor marca un número del 1-5")
