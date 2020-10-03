import os
from argparse import ArgumentParser
from sys import stderr
from packaging.pack_builder import pack_builder
from packaging.module_checker import module_checker

# License: Apache-2.0


def build(args: dict):
    build_info = []
    warning_count = 0
    error_count = 0
    pack_name = ''
    current_path = os.getcwd()

    def raise_error(err: str):
        build_info.append(f'Error: {err}')
        print(f'\033[1;31mError: {err}\033[0m', file=stderr)
    # init module_checker
    checker = module_checker()
    checker.module_path = os.path.join(current_path, "modules")
    # checking module integrity
    if not checker.check_module():
        raise_error(checker.info)
    else:
        builder = pack_builder(current_path, os.path.join(
            current_path, "modules"), checker.module_list)
        builder.args = args
        builder.build()
        build_info.append(builder.logs)
        warning_count = builder.warning_count
        error_count = builder.error_count
        pack_name = builder.filename
    return build_info, warning_count, error_count, pack_name


if __name__ == '__main__':
    def generate_parser() -> ArgumentParser:
        parser = ArgumentParser(
            description="Automatically build add-ons")
        parser.add_argument('type', default='zip',
                            help="Build type. Should be 'zip', 'mcpack' or 'clean'. If it's 'clean', all packs in 'builds/' directory will be deleted.",
                            choices=['zip', 'mcpack', 'clean'])
        parser.add_argument('-c', '--compatible', action='store_true',
                            help="Make the pack compatible to other addons. This will generate only one language file 'zh_CN.lang'.")
        parser.add_argument('-r', '--resource', nargs='*', default='all',
                            help="(Experimental) Include resource modules. Should be module names, 'all' or 'none'. Defaults to 'all'. Pseudoly accepts a path, but only module paths in 'modules' work.")
        parser.add_argument('-o', '--output', nargs='?', default='builds',
                            help="Specify the location to output packs. Default location is 'builds/' folder.")
        parser.add_argument('--hash', action='store_true',
                            help="Add a hash into file name.")
        return parser
    args = vars(generate_parser().parse_args())
    if args['type'] == 'clean':
        for i in os.listdir('builds/'):
            os.remove(os.path.join('builds', i))
        print("Deleted all packs built.")
    else:
        build(args)
