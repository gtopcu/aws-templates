
import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logger = logging.getLogger('ftpuploader')
fh = logging.FileHandler('ftplog.log')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.INFO)

logger.info('File successfully uploaded')
logger.error("Houston, we have a %s", "major problem", exc_info=1)


#############################

logger = logging.getLogger()
formatter = logging.Formatter(
    "[%(asctime)s] %(name)s {%(pathname)s:%(lineno)d} %(levelname)s -"
    " %(message)s",
    "%d-%m %H:%M:%S",
)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)
