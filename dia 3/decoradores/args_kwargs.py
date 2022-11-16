

def hello(*args, **kwargs):
  return kwargs, args


fun = hello('palabra', 10, 2, a='hola mundo', c=True, b=45)

print(fun)