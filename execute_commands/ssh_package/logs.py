
import os
import logging

username = {'user_name': os.getenv('USERNAME')}
FORMAT = '%(asctime)s - %(user_name)s - %(levelname)s - %(message)s'

logger = logging.getLogger('logs')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log_file.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
fh.setFormatter(formatter)
logger.addHandler(fh)

logger = logging.LoggerAdapter(logger, username)


