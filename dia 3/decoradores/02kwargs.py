

def empleado(**kwargs):
  for key, value in kwargs.items():
    print(value)


empleado(lenguaje = 'java', nombre='Alejandro', puesto='programador' )