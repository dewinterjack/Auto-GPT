import logging
import datetime

def setup_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    now = datetime.datetime.now()
    file_handler = logging.FileHandler('outputs/logs/autogpt_{}.log'.format(now.strftime('%Y%m%d_%H%M%S')))
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logger('info')
