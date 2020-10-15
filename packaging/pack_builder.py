import os
from hashlib import sha256
from json import load, dumps
from os.path import join
from sys import stderr
from zipfile import ZipFile, ZIP_DEFLATED


class pack_builder(object):
    def __init__(self, main_res_path: str, module_info: dict):
        self.__args = {}
        self.__warning = 0
        self.__error = False
        self.__log_list = []
        self.__filename = ""
        self.__main_res_path = main_res_path
        self.__module_info = module_info

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
    def error(self):
        return self.__error

    @property
    def filename(self):
        return self.__filename

    @property
    def log_list(self):
        return self.__log_list

    @property
    def main_resource_path(self):
        return self.__main_res_path

    @property
    def module_info(self):
        return self.__module_info

    def clean_status(self):
        self.__warning = 0
        self.__error = False
        self.__log_list = []
        self.__filename = ""

    def build(self):
        self.clean_status()
        args = self.args
        # args validation
        status, info = self.__check_args()
        if status:
            # get resource modules
            res_supp = self.__parse_includes('resource')
            # process pack name
            digest = sha256(dumps(args).encode('utf8')).hexdigest()
            pack_name = args['hash'] and f"meme-resourcepack.{digest[:7]}.{args['type']}" or f"meme-resourcepack.{args['type']}"
            self.__filename = pack_name
            # create pack
            info = f"Building pack {pack_name}"
            print(info)
            self.__log_list.append(info)
            # set output dir
            pack_name = join(args['output'], pack_name)
            # mkdir
            if os.path.exists(args['output']) and not os.path.isdir(args['output']):
                os.remove(args['output'])
            if not os.path.exists(args['output']):
                os.mkdir(args['output'])
            # all builds have these files
            pack = ZipFile(
                pack_name, 'w', compression=ZIP_DEFLATED, compresslevel=5)
            pack.write(join(self.main_resource_path,
                            "LICENSE"), arcname="LICENSE")
            pack.write(join(self.main_resource_path, "pack_icon.png"),
                       arcname="pack_icon.png")
            pack.write(join(self.main_resource_path, "manifest.json"),
                       arcname="manifest.json")
            self.__dump_language_file(pack)
            pack.write(join(self.main_resource_path, "textures/map/map_background.png"),
                       arcname="textures/map/map_background.png")
            # dump resources
            item_texture, terrain_texture = self.__dump_resources(
                res_supp, pack)
            if item_texture:
                item_texture_content = self.__merge_json(item_texture, "item")
                pack.writestr("textures/item_texture.json",
                              dumps(item_texture_content, indent=4))
            if terrain_texture:
                terrain_texture_content = self.__merge_json(
                    terrain_texture, "terrain")
                pack.writestr("textures/terrain_texture.json",
                              dumps(terrain_texture_content, indent=4))
            pack.close()
            print(f'Successfully built {pack_name}.')
            self.__log_list.append(f'Successfully built {pack_name}.')

        else:
            self.__raise_error(info)

    def __raise_warning(self, warning: str):
        print(f'\033[33mWarning: {warning}\033[0m', file=stderr)
        self.__log_list.append(f'Warning: {warning}')
        self.__warning += 1

    def __raise_error(self, error: str):
        print(f'\033[1;31mError: {error}\033[0m', file=stderr)
        print("\033[1;31mTerminate building because an error occurred.\033[0m")
        self.__log_list.append(f'Error: {error}')
        self.__log_list.append("Terminate building because an error occurred.")
        self.__error = True

    def __check_args(self):
        for item in ('type', 'compatible', 'modules', 'output', 'hash'):
            if item not in self.args:
                return False, f'Missing argument "{item}"'
        return True, None

    def __parse_includes(self, type: str) -> list:
        includes = self.args['modules'][type]
        full_list = list(
            map(lambda item: item['name'], self.module_info['modules'][type]))
        if 'none' in includes:
            return []
        elif 'all' in includes:
            return full_list
        else:
            include_list = []
            for item in includes:
                if item in full_list:
                    include_list.append(item)
                else:
                    self.__raise_warning(
                        f'Module "{item}" does not exist, skipping')
            return include_list

    def __merge_json(self, modules: list, type: str) -> dict:
        name = type == "item" and "item_texture.json" or "terrain_texture.json"
        result = {'texture_data': {}}
        for item in modules:
            texture_file = join(
                self.module_info['path'], item, "textures", name)
            content = load(open(texture_file, 'r', encoding='utf8'))
            result['texture_data'] |= content['texture_data']
        return result

    def __dump_resources(self, modules: list, pack: ZipFile):
        item_texture = []
        terrain_texture = []
        for item in modules:
            base_folder = join(self.module_info['path'], item)
            for root, _, files in os.walk(base_folder):
                for file in files:
                    if file != "module_manifest.json":
                        if file == "item_texture.json":
                            item_texture.append(item)
                        elif file == "terrain_texture.json":
                            terrain_texture.append(item)
                        else:
                            path = join(root, file)
                            arcpath = path[path.find(
                                base_folder) + len(base_folder) + 1:]
                            testpath = arcpath.replace(os.sep, "/")
                            # prevent duplicates
                            if testpath not in pack.namelist():
                                pack.write(join(root, file), arcname=arcpath)
                            else:
                                self.__raise_warning(
                                    f"Duplicated '{testpath}', skipping.")
        return item_texture, terrain_texture

    def __dump_language_file(self, pack: ZipFile):
        if self.args['compatible']:
            pack.write(join(self.main_resource_path, "texts/zh_ME.lang"),
                       arcname="texts/zh_CN.lang")
        else:
            for file in os.listdir(join(self.main_resource_path, "texts")):
                pack.write(join(self.main_resource_path, f"texts/{file}"),
                           arcname=f"texts/{file}")
