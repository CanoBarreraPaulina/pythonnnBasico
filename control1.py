mes=int(input("Para saber la estacion del año ingresa el numero del mes (1-12):"))
'''''invierno:12,1,2  prima:3,4,5 verano:6,7,8 otoño:9,10,11'''''
if mes ==12 or mes==1 or mes==2:
    print("tu mes pertenece a invierno")
elif mes>=3 and mes <=5:
    print("tu mes pertenece a primavera")
elif mes>=6 and mes<=8:
    print("tu mes pertenece a verano")
elif mes>=9 and mes<=11:
    print("tu mes pertenece a otoño")
else:
    print("el numero que ingresaste no es valido, intenta otra vez")
    