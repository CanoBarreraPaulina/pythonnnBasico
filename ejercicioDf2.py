import pandas as pd
tabla={"MES":["Enero","Febrero", "Marzo","Abril"],
    "VENTAS":[35500,44200,40780,39200],
    "GASTOS": [16780,23680,21500,20890]
}
tb=pd.DataFrame(tabla)


print(tb.mean())