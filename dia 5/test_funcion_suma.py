from unittest import TestCase
from funcion_suma import suma
import unittest


class TestFuncionSuma(TestCase):

  def test_funcion_suma(self):
    sum = suma(2, 3)
    self.assertIsNotNone(sum)
    self.assertEqual(sum, 5)


if __name__ == '__main__':
  unittest.main()
