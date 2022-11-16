

def generador():
  n = 1
  yield n

  n = n + 1
  yield n

  n = n + 1
  yield n

gen = generador()

for g in gen:
  print(g)