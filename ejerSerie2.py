import pandas as pd

def adescuento(ventas):
    return ventas * 0.9

aI = int(input("Ingrese el año inicial: "))
aF = int(input("Ingrese el año final: "))

ventasA = {}
for año in range(aI, aF + 1):
    ventas = float(input(f"Ingrese las ventas para el año {año}: "))
    ventasA[año] = ventas

serieVE = pd.Series(ventasA)

serieDE = adescuento(serieVE)

print("\nVentas originales:")
print(serieVE)

print("\nVentas con descuento del 10%:")
print(serieDE)