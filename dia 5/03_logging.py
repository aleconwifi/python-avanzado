import logging

logging.basicConfig(
  level=logging.DEBUG,
  format=f'[%(levelname)s] | %(processName)s - %(asctime)s -> %(message)s',
  datefmt='%H:%M:%S',
  filename='archivo_log.log',
  filemode='w')

x = 2
y = 5
suma = x + y

logging.info(f'El valor de x es {x}')
logging.info(f'El valor de y es {y}')
logging.info(f'La suma es {suma}')
