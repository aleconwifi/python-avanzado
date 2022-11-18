from unittest.mock import MagicMock, patch
from unittest import TestCase
from get_nationality import get_nationality_by_name
import json 
class TestGetNationaltyByName(TestCase):
  @patch("requests.get")
  def test_get_nationality_by_name(self, mock_requests):
    mock_response = MagicMock()

    mock_response.text = """    
      {"country":[{"country_id":"MX","probability":0.148},{"country_id":"AR","probability":0.13},{"country_id":"CL","probability":0.103},    {"country_id":"CO","probability":0.075},  {"country_id":"ES","probability":0.065}],"name":"Alejandro"}
    """
    mock_requests.return_value = mock_response

    country_code = get_nationality_by_name('Alejandro')
    self.assertEqual(country_code, "ES")

