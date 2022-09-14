# Evitar redondear numeros a partir de .5
# Redondear a partir del punto decimal de tu preferencia.
# how to round from specific decimal point
minimum = float(input("Introduce Numero a redondear en decimal: "))
redondeo = int(input("Introduce . Decimal de Redondeo: "))
minimum6=str(minimum).split('.')[-1]
# print(minimum[:1])
if minimum6:
    minimum1 = minimum6[:1]
    minimum2 = int(minimum1)
    if minimum2 >= redondeo:
        print(int(minimum)+1)
