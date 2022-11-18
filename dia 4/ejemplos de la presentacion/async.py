import time
from datetime import datetime
from random import randint
from asyncio import coroutine, sleep, Task, get_event_loop

info = []
results = []


#agrega un elemento cada segundo a la lista
async def generate_info():
  while True:
    await sleep(1)
    info.append(f"ago a las  {datetime.now()}")
    print('New info anadida')


#se fija si algo en la lista de info, si hay algo lo saca
async def process_info():
  while True:
    #no va a sacar nadie
    await sleep(1)
    print('Checkear por nueva info')
    if info:
      new_info = info.pop()
      results.append(new_info + "procesado")
      print("new info procesada")


loop = get_event_loop()

generator = loop.create_task(generate_info())
processor1 = loop.create_task(process_info())
processor2 = loop.create_task(process_info())

loop.run_forever()
