
permitido = True

def autenticacion(func):
  def wrapper():
    if permitido ==True:
      print('Adelante!')
      return func()
    else:
      print('Pues va a ser que no...')
  return wrapper
    

@autenticacion
def hacer_algo():
  return 'Voy a bañarme!'


hacer_algo()