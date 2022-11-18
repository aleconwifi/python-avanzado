import time

def subir_foto():
    print("s: subiendo byte 1")
    yield
    print("s: subiendo byte 2")
    yield
    print("s: subiendo byte 3")


def twitter():
    print("t: leyendo a roberto")
    yield
    print('t: discutiendo con roberto')
    yield
    print('t: postear foto')
    yield from subir_foto()
    print('t: indignado por politica')

def estudiar():
    print('e: leyendo el material')
    yield
    print('e: armando resumen')
    yield
    print('e: leyendo el resumnen')
    print('e: memorizando resumen')
    yield
    print('e: llorando')


loop([twitter(), estudiar()])