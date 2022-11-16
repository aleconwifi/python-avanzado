

def funciona(funcionb):
  def funcionc(*args, **kwargs):
    print('Cosas que quiero que ocurran antes de la ejecucion')
    result = funcionb(*args, **kwargs)
    print('Cosas que quiero que ocurran despues de la ejecucion ')
    return result

  return funcionc


@funciona
def resta(a,b):
  print( a - b )

@funciona
def suma(a,b):
  print( a + b )


#print_name = start_end_decorator(print_name)

resta(4,5)