import logging

logging.basicConfig(
  level=logging.DEBUG,
  format=f'[%(levelname)s] | %(processName)s - %(asctime)s -> %(message)s',
  datefmt='%H:%M:%S')


def messages():
  logging.debug("This is a debug message")
  logging.info("This is a info message")
  logging.warning("This is a warning message")
  logging.error("This is a error message")
  logging.critical("This is a critical message")


messages()
