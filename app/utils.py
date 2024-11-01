import logging

from configparser import ConfigParser

# -----------------------------------
# config init

config = ConfigParser()
config.read('config.ini')

# -----------------------------------
# logger

formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(name)s]: %(message)s')

def setup_logger(name):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(config.get('logger', 'filename'))        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(config.get('logger', 'level'))
    logger.addHandler(handler)

    return logger

server_logger = setup_logger('server')
db_logger = setup_logger('db')

# -----------------------------------
# utils