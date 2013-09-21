import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/dangerzone_dev.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
