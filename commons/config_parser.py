import json
from commons.arg_parser import ArgParser


class ConfigParser:

    def __init__(self, file_path):
        self._arg = ArgParser()
        with open(file_path, 'r') as fd:
            self._conf = json.load(fd)

    @property
    def datetime_format(self):
        return None

    @property
    def user_account_column(self):
        return None

    @property
    def global_db_path(self):
        return None

    @property
    def snapshot_db_path(self):
        return None

    @property
    def sync_config_db_path(self):
        return None

    @property
    def device_db_db_path(self):
        return None

    @property
    def global_db_table_list(self):
        return None

    @property
    def snapshot_db_table_list(self):
        return None

    @property
    def sync_config_db_table_list(self):
        return None

    @property
    def device_db_db_table_list(self):
        return None
