import logging

logging.basicConfig(
  level=logging.DEBUG,
  format=f'[%(levelname)s] | %(processName)s - %(asctime)s -> %(message)s',
  datefmt='%H:%M:%S',
  filename='archivo_log.log',
  filemode='w')

a = 5
b = 0
d = 6
try:
  c = a / b

except Exception as e:
  logging.exception("Exception ocurred")

try:
  c = d / b

except Exception as e:
  logging.exception("Exception ocurred")
