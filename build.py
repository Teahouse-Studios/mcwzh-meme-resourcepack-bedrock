import os
from argparse import ArgumentParser
from hashlib import sha256
from json import load, dump, dumps
from sys import stderr
from zipfile import ZipFile, ZIP_DEFLATED


# License: Apache-2.0


class builder(object):
    def __init__(self):
        self.__args = {}
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, value: dict):
        self.__args = value

    @property
    def warning_count(self):
        return self.__warning

    @property
    def error_count(self):
        return self.__error

    @property
    def filename(self):
        return self.__filename != "" and self.__filename or "Did not build any pack."

    @property
    def logs(self):
        return self.__log_list and ''.join(self.__log_list) or "Did not build any pack."

    def clean_status(self):
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""

    def build(self):
        self.clean_status()
        args = self.args
        # check module name first
        checker = module_checker()
        if checker.check_module():
            # process args
            res_supp = self.__parse_includes(
                args['resource'], checker.module_list)
            # process pack name
            digest = sha256(dumps(args).encode('utf8')).hexdigest()
            pack_name = args['hash'] and f"meme-resourcepack.{digest[:7]}.{args['type']}" or f"meme-resourcepack.{args['type']}"
            self.__filename = pack_name
            # create pack
            info = f"Building pack {pack_name}"
            print(info)
            self.__log_list.append(f"{info}\n")
            # set output dir
            output_dir = 'output' in args and args['output'] or 'builds'
            pack_name = os.path.join(output_dir, pack_name)
            # mkdir
            if os.path.exists(output_dir) and not os.path.isdir(output_dir):
                os.remove(output_dir)
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            # all builds have these files
            pack = ZipFile(
                pack_name, 'w', compression=ZIP_DEFLATED, compresslevel=5)
            pack.write(os.path.join(os.path.dirname(
                __file__), "LICENSE"), arcname="LICENSE")
            pack.write(os.path.join(os.path.dirname(__file__), "meme_resourcepack/pack_icon.png"),
                       arcname="meme_resourcepack/pack_icon.png")
            pack.write(os.path.join(os.path.dirname(__file__), "meme_resourcepack/manifest.json"),
                       arcname="meme_resourcepack/manifest.json")
            for file in os.listdir(os.path.join(os.path.dirname(__file__), "meme_resourcepack/texts")):
                pack.write(os.path.join(os.path.dirname(__file__), f"meme_resourcepack/texts/{file}"),
                           arcname=f"meme_resourcepack/texts/{file}")
            pack.write(os.path.join(os.path.dirname(__file__), "meme_resourcepack/textures/map/map_background.png"),
                       arcname="meme_resourcepack/textures/map/map_background.png")
            # dump resources
            item_texture, terrain_texture = self.__dump_resources(
                res_supp, pack)
            if item_texture:
                item_texture_content = self.__merge_json(item_texture, "item")
                pack.writestr("meme_resourcepack/textures/item_texture.json",
                              dumps(item_texture_content, indent=4))
            if terrain_texture:
                terrain_texture_content = self.__merge_json(
                    terrain_texture, "terrain")
                pack.writestr("meme_resourcepack/textures/terrain_texture.json",
                              dumps(terrain_texture_content, indent=4))
            pack.close()
            print("Build successful.")
        else:
            self.__raise_error(checker.info)

    def __raise_warning(self, warning: str):
        print(f'\033[33mWarning: {warning}\033[0m', file=stderr)
        self.__log_list.append(f'Warning: {warning}')
        self.__warning += 1

    def __raise_error(self, error: str):
        print(f'\033[1;31mError: {error}\033[0m', file=stderr)
        print("\033[1;31mTerminate building because an error occurred.\033[0m")
        self.__log_list.append(f'Error: {error}')
        self.__log_list.append("Terminate building because an error occurred.")
        self.__error += 1

    def __parse_includes(self, includes: list, fulllist: list) -> list:
        if 'none' in includes:
            return []
        elif 'all' in includes:
            return fulllist
        else:
            include_list = []
            for item in includes:
                if item in fulllist:
                    include_list.append(item)
                elif self.__convert_path_to_module(os.path.normpath(item)) in fulllist:
                    include_list.append(
                        self.__convert_path_to_module(os.path.normpath(item)))
            return include_list

    def __convert_path_to_module(self, path: str) -> str:
        return load(open(os.path.join(os.path.dirname(__file__), path, "module_manifest.json"), 'r', encoding='utf8'))['name']

    def __merge_json(self, modules: list, type: str) -> dict:
        name = type == "item" and "item_texture.json" or "terrain_texture.json"
        result = {'texture_data': {}}
        for item in modules:
            texture_file = os.path.join(os.path.dirname(
                __file__), "modules", item, "textures", name)
            content = load(open(texture_file, 'r', encoding='utf8'))
            result['texture_data'].update(content['texture_data'])
        return result

    def __dump_resources(self, modules: list, pack: zipfile.ZipFile) -> (list, list):
        item_texture = []
        terrain_texture = []
        for item in modules:
            base_folder = os.path.join(os.path.dirname(
                __file__), "modules", item)
            for root, dirs, files in os.walk(base_folder):
                for file in files:
                    if file != "module_manifest.json":
                        if file == "item_texture.json":
                            item_texture.append(item)
                        elif file == "terrain_texture.json":
                            terrain_texture.append(item)
                        else:
                            path = os.path.join(root, file)
                            arcpath = os.path.join("meme_resourcepack", path[path.find(
                                base_folder) + len(base_folder) + 1:])
                            testpath = arcpath.replace(os.sep, "/")
                            # prevent duplicates
                            if testpath not in pack.namelist():
                                pack.write(os.path.join(
                                    root, file), arcname=arcpath)
                            else:
                                self.__raise_warning(
                                    f"Duplicated '{testpath}', skipping.")
        return item_texture, terrain_texture


class module_checker(object):
    def __init__(self):
        self.__status = True
        self.__checked = False
        self.__res_list = []
        self.__manifests = {}
        self.__info = ''

    @property
    def info(self):
        return self.__info

    @property
    def module_list(self):
        if not self.__checked:
            self.check_module()
        return self.__status and self.__res_list or []

    @property
    def manifests(self):
        if not self.__checked:
            self.check_module()
        return self.__status and self.__manifests or {}

    def clean_status(self):
        self.__status = True
        self.__checked = False
        self.__res_list = []
        self.__manifests = {}
        self.__info = ''

    def check_module(self):
        self.clean_status()
        base_folder = os.path.join(os.path.dirname(__file__), "modules")
        res_list = []
        for module in os.listdir(base_folder):
            manifest = os.path.join(
                base_folder, module, "module_manifest.json")
            if os.path.exists(manifest) and os.path.isfile(manifest):
                data = load(open(manifest, 'r', encoding='utf8'))
                name = data['name']
                if name in res_list:
                    self.__checked = True
                    self.__status = False
                    self.__info = f'Conflict name {name}.'
                    return False
                else:
                    self.__manifests[name] = data['description']
                    res_list.append(name)
            else:
                self.__checked = True
                self.__status = False
                self.__info = f"Bad module '{module}', no manifest file."
                return False
        self.__checked = True
        self.__status = True
        self.__res_list = res_list
        return True


def generate_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Automatically build add-ons")
    parser.add_argument('type', default='zip',
                        help="Build type. Should be 'zip', 'mcpack' or 'clean'. If it's 'clean', all packs in 'builds/' directory will be deleted.",
                        choices=['zip', 'mcpack', 'clean'])
    parser.add_argument('-r', '--resource', nargs='*', default='all',
                        help="(Experimental) Include resource modules. Should be module names, 'all' or 'none'. Defaults to 'all'. Pseudoly accepts a path, but only module paths in 'modules' work.")
    parser.add_argument(
        '-o', '--output', help="Specify the location to output packs. Default location is 'builds/' folder.")
    parser.add_argument('--hash', action='store_true',
                        help="Add a hash into file name.")
    return parser


if __name__ == '__main__':
    args = vars(generate_parser().parse_args())
    if args['type'] == 'clean':
        for i in os.listdir('builds/'):
            os.remove(os.path.join('builds', i))
        print("Deleted all packs built.")
    else:
        pack_builder = builder()
        pack_builder.args = args
        pack_builder.build()
