from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restapi.settings import db_settings
from sqlalchemy.pool import NullPool
from contextlib import contextmanager


def connect(dbuser, dbpass, dbhost, dbname, dbschema):
    connection = create_engine('postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(dbuser, dbpass, dbhost, dbname),
                               connect_args={'options': '-csearch_path={}'.format(dbschema)}, client_encoding='utf8',
                               poolclass=NullPool)
    return connection


@contextmanager
def DBConnection():
    dbuser = db_settings.get('dbuser')
    dbpass = db_settings.get('dbpass')
    dbhost = db_settings.get('dbhost')
    dbname = db_settings.get('dbname')
    dbschema = db_settings.get('dbschema')

    connection = connect(dbuser, dbpass, dbhost, dbname, dbschema)
    db_session = sessionmaker(bind=connection)

    session = db_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e