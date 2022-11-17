def frutas():
    yield "pera"
    print('frutas 2')
    yield "manzana"
    yield "banana"

def cosas():
    yield "espada"
    yield "coche"
    yield from frutas()
    yield "celular"


c = cosas()

for i in c:
    print(i)