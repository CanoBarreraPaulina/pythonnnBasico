respuestas = (0.58, 9, 2, 3, 37, 5, 75, 4)


sueño1= int(respuestas[3]) + int(respuestas[7])
sueño2 = int(respuestas[2]) + int(respuestas[3]) + int(respuestas[5])
dientes= int(respuestas [4])-int(respuestas[5])

print(f'''
1. Los humanos tenemos {respuestas[2]} ojos en la cara.
2. Un humano adulto tiene {dientes} dientes dentro de su boca.
3. Un feto tarda {respuestas[1]} meses en gestarse antes de nacer.
4. La expectativa de vida en México es de alrededor de {respuestas[6]} años.
5. Las horas de sueño al día recomendadas para adultos jóvenes son entre {sueño1} y {sueño2} horas.
6. El récord actual de velocidad en 100 metros (09/05/2020) fue establecido por Usain Bolt y es de {respuestas[0]} segundos.
''')
