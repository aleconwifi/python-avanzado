import requests
import json 

def get_nationality_by_name(name):
  url = 'https://api.nationalize.io/?name={}'.format(name)
  response = requests.get(url).text
  
  country_code = json.loads(response)['country'][0]['country_id']
  return country_code


