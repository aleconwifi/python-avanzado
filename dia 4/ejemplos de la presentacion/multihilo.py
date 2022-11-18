import time
from datetime import datetime
from random import randint
from threading import Thread

info = []
results = []


#agrega un elemento cada segundo a la lista
def generate_info():
  while True:
    time.sleep(1)
    info.append(f"ago a las  {datetime.now()}")
    print('New info anadida')


#se fija si algo en la lista de info, si hay algo lo saca
def process_info():
  while True:
    time.sleep(1)
    print('Checkear por nueva info')
    if info:
      new_info = info.pop()
      results.append(new_info + "procesado")
      print("new info procesada")


generator = Thread(target=generate_info)
processor1 = Thread(target=process_info)
processor2 = Thread(target=process_info)

generator.start()
processor1.start()
processor2.start()

generator.join()
processor1.join()
processor2.join()
