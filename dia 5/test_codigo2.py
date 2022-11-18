from codigo2 import capital_case, escribir


def test_capital_case():
  assert capital_case('alejandro') == 'Alejandro'
  assert capital_case('ALEJANDRO') == 'Alejandro'
  assert capital_case('Alejandro') == 'Alejandro'
  assert capital_case('aleJandrO') == 'Alejandro'

def test_temp_dir(tmpdir):
  data_in = 'Data que estoy escribiendo para probar'
  fpath = f'{tmpdir}/test.txt'
  escribir(fpath, data_in)

  with open(fpath) as file_out:
    data_out = file_out.read()

  assert data_in == data_out
  assert data_out == data_in
  assert str(data_out) == str(data_out)


