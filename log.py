import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt = '%d-%m-%Y  %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('books')
logger.debug('this is a messsage')
logger.info('this will not show up')
logger.warning('this will')
logger.critical('a crictical error occured')

