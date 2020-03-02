import os
# import logging

# from logging.handlers import RotatingFileHandler
from test import app as application

# application.logger.setLevel(logging.INFO)
# handler = RotatingFileHandler('application.log',
#                                maxBytes=10000, backupCount=5)
# formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
# application.logger.addHandler(handler)
AWW = 12345

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

