def numero_es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
    return

def test_funcion(funcion_a_probar, num_de_errores, contador, parametros=[], resultado_esperado=None):
    resultado_test = funcion_a_probar(*parametros)
    print(f'Test {contador}: Resultado esperado es `{resultado_esperado}`, obtuvimos `{resultado_test}`')
    if resultado_test != resultado_esperado:
        num_de_errores += 1
        
    return num_de_errores


print("== Tests numero_es_par==\n")

contador_de_tests = 0
errores = 0

contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[2], resultado_esperado=True)
contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[3], resultado_esperado=False)
contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[0], resultado_esperado=True)
contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[127], resultado_esperado=False)
contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[-88], resultado_esperado=True)
contador_de_tests += 1
errores = test_funcion(numero_es_par, errores, contador_de_tests, parametros=[-1349], resultado_esperado=False)

print(f'\nErrores encontrados: {errores}')