



def autenticacion(permitido=True):
  def wrapper(func):
    def wrapper_2():
      if permitido ==True:
        print('Adelante!')
        func()
      else:
        print('Pues va a ser que no...')
    return wrapper_2

  return wrapper
    

@autenticacion(False)
def hacer_algo():
  return 'Voy a bañarme!'


hacer_algo()