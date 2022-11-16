

def funcion_generadora_prints():
  print('GENERADOR: Se va a generar el primer dato')
  yield "valor generado 1"

  print('GENERADOR: Se va a genera el segundo datos')
  yield "valor generado 2"

  print('GENERADOR: Se va a generar el tener dato')
  yield "valor generado 3 "

  print('GENERADOR: termina y lanzara automaticamente una excepcion StopIteration')

generador = funcion_generadora_prints()

for i in generador:
  print(i)