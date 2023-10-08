euros = float(input("Introduce la cantidad en euros que quieres convertir: "))
cambio = int(input("Para convertirlo a dólares marca 1 a pesos 2, a yuanes 3, a libras 4 y a francos 5 : "))
if cambio == 1:
    conversion_dolares = euros * 0.94
    print(f"Equivale a {conversion_dolares} dólares")
elif cambio == 2:
    conversion_pesos = euros * 19.25
    print(f"Equivale a {conversion_pesos} pesos")
elif cambio == 3:
    conversion_yuanes = euros * 7.63
    print(f"Equivale a {conversion_yuanes} yuanes")
elif cambio == 4:
    conversion_libras = euros * 1.15
    print(f"Equivale a {conversion_libras} libras")
elif cambio == 5:
    conversion_francos = euros * 0.96
    print(f"Equivale a {conversion_francos} francos")
else:
    print("Por favor marca un número del 1-5")
