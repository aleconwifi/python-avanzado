import time

def calcular_tiempo(func):
  def wrapper(*args, **kwargs):
    if 
    start = time.time()
    result =  func(*args, **kwargs)
    print('El tiempo total es', time.time() - start)
    return result


  return wrapper


@calcular_tiempo
def suma(a,b):
  time.sleep(3)
  return a + b


@calcular_tiempo()
def imprimir():
  time.sleep(3)

  return 'Hola como estas'

#print(suma(10,20))
print(imprimir())