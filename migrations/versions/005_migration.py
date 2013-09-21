from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
crime = Table('crime', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('description', String),
    Column('place', String),
    Column('date', DateTime),
    Column('longitude', Float),
    Column('latitude', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['crime'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['crime'].drop()
