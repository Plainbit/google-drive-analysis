from commons.config_parser import ConfigParser
from commons.arg_parser import ArgParser
from commons import output


class Main:

    def __init__(self):

        # prepare some modules
        self._arg = ArgParser()
        self._conf = ConfigParser('./config.json')

        # step 1. get information about login

        # step 2. get list about synced folders and files

        # step 3. parse sync log

        # step 4. result output


if __name__ == "__main__":
    Main()
