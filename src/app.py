#!/usr/local/bin/python3

"""
RESTful API
"""
import logging
import os

import connexion

from src import WORKDIR, database_config
from src.config import log
from src.models import db

log.init()
logger = logging.getLogger('app')

SWAGGER = os.path.join(WORKDIR, 'swagger')
logger.info('Path of swagger file: {path}'.format(path=SWAGGER))
app = connexion.App(__name__, port=8080, specification_dir=SWAGGER)
app.add_api('employee.yaml')
application = app.app
logger.info('Database configutation: {config}'.format(config=database_config))
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{0:s}:{1:s}@{2:s}:{3:d}/{4:s}'.format(
    database_config['username'], database_config['password'], database_config['host'], database_config['port'],
    database_config['dbname'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)
db.create_all(app=application)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=app.port)
