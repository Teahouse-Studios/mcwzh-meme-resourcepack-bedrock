import os
from hashlib import sha256
from json import load, dumps
from sys import stderr
from zipfile import ZipFile, ZIP_DEFLATED
from packaging.module_checker import module_checker


class pack_builder(object):
    def __init__(self, main_res_path: str, module_path: str, module_list: list):
        self.__args = {}
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""
        self.__main_res_path = main_res_path
        self.__module_path = module_path
        self.__module_list = module_list

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

    @property
    def main_resource_path(self):
        return self.__main_res_path

    @property
    def module_path(self):
        return self.__module_path

    @property
    def module_list(self):
        return self.__module_list

    def clean_status(self):
        self.__warning = 0
        self.__error = 0
        self.__log_list = []
        self.__filename = ""

    def build(self):
        self.clean_status()
        args = self.args
        # args validation
        status, info = self.__check_args()
        if status:
            # process args
            res_supp = self.__parse_includes(
                args['resource'], self.module_list)
            # process pack name
            digest = sha256(dumps(args).encode('utf8')).hexdigest()
            pack_name = args['hash'] and f"meme-resourcepack.{digest[:7]}.{args['type']}" or f"meme-resourcepack.{args['type']}"
            self.__filename = pack_name
            # create pack
            info = f"Building pack {pack_name}"
            print(info)
            self.__log_list.append(f"{info}\n")
            # set output dir
            pack_name = os.path.join(args['output'], pack_name)
            # mkdir
            if os.path.exists(args['output']) and not os.path.isdir(args['output']):
                os.remove(args['output'])
            if not os.path.exists(args['output']):
                os.mkdir(args['output'])
            # all builds have these files
            pack = ZipFile(
                pack_name, 'w', compression=ZIP_DEFLATED, compresslevel=5)
            pack.writestr("LICENSE", self.__handle_license())
            pack.write(os.path.join(self.main_resource_path, "meme_resourcepack/pack_icon.png"),
                       arcname="meme_resourcepack/pack_icon.png")
            pack.write(os.path.join(self.main_resource_path, "meme_resourcepack/manifest.json"),
                       arcname="meme_resourcepack/manifest.json")
            self.__dump_language_file(pack)
            pack.write(os.path.join(self.main_resource_path, "meme_resourcepack/textures/map/map_background.png"),
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
        self.__error += 1

    def __check_args(self):
        for item in ('type', 'compatible', 'resource', 'output', 'hash'):
            if item not in self.args:
                return False, f'Missing argument "{item}"'
        return True, None

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
        return load(open(os.path.join(path, "module_manifest.json"), 'r', encoding='utf8'))['name']

    def __merge_json(self, modules: list, type: str) -> dict:
        name = type == "item" and "item_texture.json" or "terrain_texture.json"
        result = {'texture_data': {}}
        for item in modules:
            texture_file = os.path.join(
                self.module_path, item, "textures", name)
            content = load(open(texture_file, 'r', encoding='utf8'))
            result['texture_data'].update(content['texture_data'])
        return result

    def __dump_resources(self, modules: list, pack: ZipFile):
        item_texture = []
        terrain_texture = []
        for item in modules:
            base_folder = os.path.join(self.module_path, item)
            for root, _, files in os.walk(base_folder):
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

    def __dump_language_file(self, pack: ZipFile):
        if 'compatible' in self.args and self.args['compatible']:
            pack.write(os.path.join(self.main_resource_path, "meme_resourcepack/texts/zh_ME.lang"),
                       arcname="meme_resourcepack/texts/zh_CN.lang")
        else:
            for file in os.listdir(os.path.join(self.main_resource_path, "meme_resourcepack/texts")):
                pack.write(os.path.join(self.main_resource_path, f"meme_resourcepack/texts/{file}"),
                           arcname=f"meme_resourcepack/texts/{file}")

    def __handle_license(self):
        return ''.join(
            item[1] for item in enumerate(
                open(os.path.join(self.main_resource_path, "LICENSE"), 'r', encoding='utf8')) if 9 < item[0] < 391)
