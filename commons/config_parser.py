import json
from commons.arg_parser import ArgParser
from errors.conf import ConfFilePathError

conf = None


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


def get_conf(config_path=None):
    global conf

    if conf:
        return conf

    elif config_path is not None:
        conf = ConfigParser(config_path)
        return conf

    else:
        raise ConfFilePathError()
