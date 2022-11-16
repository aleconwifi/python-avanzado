class AlCuadrado:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 9:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result


eleva_al_cuadrado = AlCuadrado()
for i in eleva_al_cuadrado:
    print(i)
