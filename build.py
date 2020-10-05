import os
from argparse import ArgumentParser
from os.path import join
from packaging.pack_builder import pack_builder
from packaging.module_checker import module_checker

# License: Apache-2.0


def build(args: dict):
    build_info = []
    current_path = os.getcwd()
    # init module_checker
    checker = module_checker()
    checker.module_path = join(current_path, "modules")
    # checking module integrity
    checker.check_module()
    build_info.extend(checker.info_list)
    builder = pack_builder(current_path, join(
        current_path, "modules"), checker.module_list)
    builder.args = args
    builder.build()
    build_info.append(builder.log_list)
    return build_info, builder.warning_count, builder.error_count, builder.filename


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

    def handle_args(args: dict):
        module_types = ('resource', )
        args['modules'] = {key: args.pop(key) for key in module_types}
        return args

    args = handle_args(vars(generate_parser().parse_args()))
    if args['type'] == 'clean':
        for i in os.listdir('builds/'):
            os.remove(join('builds', i))
        print("Deleted all packs built.")
    else:
        build(args)
