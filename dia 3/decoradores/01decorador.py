



def funciona(funcionb):
  def funcionc():
    print('Cosas que quiero que ocurran antes de la ejecucion')
    funcionb()
    print('Cosas que quiero que ocurran despues de la ejecucion ')

  return funcionc


@funciona
def print_name():
  print('Alejandro')




#print_name = start_end_decorator(print_name)

print_name()