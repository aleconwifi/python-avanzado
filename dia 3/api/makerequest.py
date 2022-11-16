
import requests

url = "https://apirest.datacampero.repl.co"


res = requests.get(f"{url}/tareas")
res.raise_for_status()
datos = res.json()

datos