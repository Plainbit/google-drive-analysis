from commons.config_parser import get_conf
from commons.arg_parser import get_arg
from commons import output


class Main:

    def __init__(self):

        # prepare some modules
        _arg = get_arg()
        _conf = get_conf(_arg.get_config_path())

        # step 1. get information about login

        # step 2. get list about synced folders and files

        # step 3. parse sync log

        # step 4. result output


if __name__ == "__main__":
    Main()
