import logging

# Create a custom logger
logger = logging.getLogger('my_logger')

# Configure the custom logger
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('my_app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Logging message using th customer logger
logger.debug('This is a debug message from my_logger')
logger.info('This is an info message from my_logger')
logger.warning('This is a warning message from my_logger')
logger.error('This is a Error message from my_logger')
logger.critical('This is a Critical message from my_logger')
