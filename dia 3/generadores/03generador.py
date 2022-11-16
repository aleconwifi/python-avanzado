
import sys

lista = [2,4,6,8,10]

lista_al_cuadrado = [i ** 2 for i in lista]

print(lista_al_cuadrado)
print( 'Size List', sys.getsizeof(lista_al_cuadrado))

generador_al_cuadrado = (i ** 2 for i in lista)



for i in generador_al_cuadrado:
  print(i)


print( 'Size Generator', sys.getsizeof(generador_al_cuadrado))
