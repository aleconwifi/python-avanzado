def capital_case(x):
  return x.capitalize()


def escribir(fpath, data_in):
  with open(fpath, 'w') as file_in:
    file_in.write(data_in)