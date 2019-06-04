import argparse
import os


class ArgParser:

    def __init__(self):
        self._arg_parser = argparse.ArgumentParser(
            description='Super Windows Artifact Parser'
        )
        self._set_arguments()
        self._args = self._arg_parser.parse_args()

    def _set_arguments(self):
        _input_options = self._arg_parser.add_mutually_exclusive_group()
        _output_options = self._arg_parser.add_mutually_exclusive_group()

        _input_options.required = True
        _output_options.required = True

        _input_options.add_argument(
            '-d', '--dir',
            dest='input_dir_path',
            action='store',
            type=str,
            default=None,
            help='Artifact directory path to want to analysis'
        )

        _input_options.add_argument(
            '--lang',
            dest='lang',
            action='store',
            type=str,
            default='ko',
            help="Language option for output column ('ko' or 'en')"
        )

        _output_options.add_argument(
            '-c', '--csv',
            dest='output_path',
            action='store',
            type=str,
            default=None,
            help='Output path to want to store'
        )

    @property
    def get_input_dir_path(self):
        if hasattr(self._args, 'input_dir_path'):
            if self._args.input_dir_path is not None:
                if os.path.isdir(self._args.input_dir_path):
                    return self._args.input_dir_path
        return None

    @property
    def get_output_csv_path(self):
        if hasattr(self._args, 'csv_path'):
            if self._args.csv_path is not None:
                return self._args.csv_path
        return None
