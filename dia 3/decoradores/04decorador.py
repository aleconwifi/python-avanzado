
def revisar(func):
  def wrapper(a,b):
    if b == 0:
      return "No se puede dividir entre 0"

    return func(a,b)

  return wrapper

@revisar
def division(a,b):
  return a / b


print(division(10,0))