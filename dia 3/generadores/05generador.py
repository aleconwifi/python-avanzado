

def pintar_azul(lista_cajas):
  for caja in lista_cajas:
    if caja =='Blanco':
      yield 'Azul'
    elif caja == 'Rojo':
      yield 'Morado'
    else:
      yield caja



lista_cajas = ['Blanco', 'Rojo', 'Negro']

gen = pintar_azul(lista_cajas)


for caja in gen:
  print(caja)
