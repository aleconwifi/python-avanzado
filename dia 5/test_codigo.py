from codigo import suma, is_greather_than, login
import pytest

def test_suma():
  assert suma(1, 3) == 4


def test_is_greather_than():
  assert is_greather_than(10, 2)


@pytest.mark.parametrize("input_a, input_b, result", [(3, 2, 5), (2, 3, 5),
                                                      (suma(3, 2), 5, 10),
                                                      (3, suma(2, 5), 10)])
def test_suma_multi(input_a, input_b, result):
  assert suma(input_a, input_b) == result


def test_login_pass():
  assert login('admin', '12345')

def test_login_fails():
  assert not login('admin', '1234566545') 
  assert not login('admin233', '12345') 
  assert not login('admin233', '12345434234') 