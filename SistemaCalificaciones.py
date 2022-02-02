# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
# El usuario proporcionará un valor entre 0 y 10.
calificacion = int(input("Introduzca califcacion de (0-10): "))
mensaje = None
# Si está entre 9 y 10: imprimir una A
if 9 <= calificacion <= 10:
    mensaje = "A"
    print(f"Su Calificacion es {calificacion} has sacado {mensaje}")
# Si está entre 8 y menor a 9: imprimir una B
elif 8 <= calificacion < 9:
    mensaje = "B"
    print(f"Su Calificacion es {calificacion} has sacado {mensaje}")
# Si está entre 7 y menor a 8: imprimir una C
elif 7 <= calificacion < 8:
    mensaje = "C"
    print(f"Su Calificacion es {calificacion} has sacado {mensaje}")
# Si está entre 6 y menor a 7: imprimir una D
elif 6 <= calificacion < 7:
    mensaje = "D"
    print(f"Su Calificacion es {calificacion} has sacado {mensaje}")
# Si está entre 0 y menor a 6: imprimir una F
elif 0 <= calificacion < 6:
    mensaje = "F"
    print(f"Su Calificacion es {calificacion} has sacado {mensaje}")
# cualquier otro valor debe imprimir: Valor desconocido
else:
    mensaje = "Valor desconocido"
    print(mensaje)