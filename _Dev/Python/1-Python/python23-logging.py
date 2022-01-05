

import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logger = logging.getLogger('ftpuploader')
fh = logging.FileHandler('ftplog.log')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.INFO)

logger.info('File successfully uploaded')
logger.error("Houston, we have a %s", "major problem", exc_info=1)
        