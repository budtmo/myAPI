#!/usr/local/bin/python3

"""
RESTful API
"""
import logging

import connexion

from src import SWAGGER_PATH
from src import settings
from src.config import log
from src.models import db

log.init()
logger = logging.getLogger('app')

logger.info('Path of swagger file: {path}'.format(path=SWAGGER_PATH))
app = connexion.App(__name__, specification_dir=SWAGGER_PATH)
app.add_api('employee.yaml')
application = app.app
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{0:s}:{1:s}@{2:s}:{3:d}/{4:s}'.format(
    settings.DB_USER, settings.DB_PASS, settings.DB_HOST, settings.DB_PORT, settings.DB_NAME)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)
db.create_all(app=application)

if __name__ == '__main__':
    application.run(port=settings.APP_PORT)
