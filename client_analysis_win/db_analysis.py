import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBHelper:

    def __init__(self, root_path, db_path):

        _db_path = os.path.join(root_path, db_path)
        _connection_info = f'sqlite://{_db_path}'
        _engine = create_engine(_connection_info)
        self._session = sessionmaker(bind=_engine)

    @property
    def session(self):
        return self._session()
