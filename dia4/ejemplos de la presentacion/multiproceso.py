import time
from datetime import datetime
from random import randint
from multiprocessing import Process, Manager

shared_memory = Manager()

info = shared_memory.list([])
results = shared_memory.list([])


#agrega un elemento cada segundo a la lista
def generate_info(info):
  while True:
    time.sleep(1)
    info.append(f"ago a las  {datetime.now()}")
    print('New info anadida')


#se fija si algo en la lista de info, si hay algo lo saca
def process_info(info, results):
  while True:
    time.sleep(1)
    print('Checkear por nueva info')
    if info:
      new_info = info.pop()
      results.append(new_info + "procesado")
      print("new info procesada")


generator = Process(target=generate_info, args=[info])
processor1 = Process(target=process_info, args=[info, results])
processor2 = Process(target=process_info, args=[info, results])

generator.start()
processor1.start()
processor2.start()

generator.join()
processor1.join()
processor2.join()