import zipfile
import json
import argparse
import os
import sys

# Apache 2.0


def main():
    parser = generate_parser()
    args = vars(parser.parse_args())
    if args['type'] == 'clean':
        for i in os.listdir('builds/'):
            os.remove('builds/' + i)
        print("Deleted all packs built.")
    else:
        pack_builder = builder()
        pack_builder.set_args(args)
        pack_builder.build()


class builder(object):
    def __init__(self):
        self.__args = {}
        self.__warning = 0
        self.__error = 0
        self.__logs = ""
        self.__filename = ""

    def set_args(self, new_args: dict):
        self.__args = new_args

    def get_warning_count(self):
        return self.__warning

    def get_error_count(self):
        return self.__error

    def get_filename(self):
        if self.__filename == "":
            return "Did not build any pack."
        else:
            return self.__filename

    def get_logs(self):
        if self.__logs == "":
            return "Did not build any pack."
        else:
            return self.__logs

    def clean_status(self):
        self.__warning = 0
        self.__error = 0
        self.__logs = ""
        self.__filename = ""

    def build(self):
        self.clean_status()
        args = self.__args
        # check module name first
        checker = module_checker()
        if checker.check_module():
            # process args
            res_supp = self.__parse_includes(
                args['resource'], checker.get_module_list())
            # process pack name
            file_ext = args['type']
            if args['hash']:
                sha256 = hashlib.sha256(json.dumps(
                    args).encode('utf8')).hexdigest()
                pack_name = f"meme-resourcepack.{sha256[:7]}.{file_ext}"
            else:
                pack_name = f"meme-resourcepack.{file_ext}"
            self.__filename = pack_name
            # create pack
            info = f"Building pack {pack_name}"
            print(info)
            self.__logs += f"{info}\n"
            # set output dir
            if 'output' in args and args['output']:
                output_dir = args['output']
            else:
                output_dir = "builds"
            pack_name = os.path.join(output_dir, pack_name)
            # mkdir
            if os.path.exists(output_dir) and not os.path.isdir(output_dir):
                os.remove(output_dir)
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            # all builds have these files
            pack = zipfile.ZipFile(
                pack_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5)
            pack.write("LICENSE")
            pack.write("meme_resourcepack/pack_icon.png")
            pack.write("meme_resourcepack/manifest.json")
            for file in os.listdir("meme_resourcepack/texts"):
                pack.write("meme_resourcepack/texts/" + file)
            pack.write("meme_resourcepack/textures/map/map_background.png")
            # dump resources
            item_texture, terrain_texture = self.__dump_resources(
                pack, res_supp)
            if item_texture:
                item_texture_content = self.__merge_json(item_texture, "item")
                pack.writestr("meme_resourcepack/textures/item_texture.json",
                              json.dumps(item_texture_content, indent=4))
            if terrain_texture:
                terrain_texture_content = self.__merge_json(
                    terrain_texture, "terrain")
                pack.writestr("meme_resourcepack/textures/terrain_texture.json",
                              json.dumps(terrain_texture_content, indent=4))
            pack.close()
            print("Build successful.")
        else:
            error = 'Error: ' + checker.get_info()
            print(f"\033[1;31m{error}\033[0m", file=sys.stderr)
            self.__logs += f"{error}\n"
            self.__error += 1
            print(
                "\033[1;31mTerminate building because an error occurred.\033[0m")

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
        with open(os.path.join(path, "module_manifest.json"), 'r', encoding='utf8') as f:
            manifest = json.load(f)
        name = manifest['name']
        return name

    def __merge_json(self, modules: list, type: str) -> dict:
        if type == "item":
            name = "item_texture.json"
        elif type == "terrain":
            name = "terrain_texture.json"
        else:
            name = ""
        result = {'texture_data': {}}
        for item in modules:
            texture_file = os.path.join(os.path.dirname(
                __file__), "modules", item, "textures", name)
            with open(texture_file, 'r', encoding='utf8') as f:
                content = json.load(f)
            result['texture_data'].update(content['texture_data'])
        return result

    def __dump_resources(self, pack: zipfile.ZipFile, modules: list) -> (list, list):
        item_texture = []
        terrain_texture = []
        for item in modules:
            base_folder = os.path.join("modules", item)
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
                                warning = f"Warning: Duplicated '{testpath}', skipping."
                                print(
                                    f"\033[33m{warning}\033[0m", file=sys.stderr)
                                self.__logs += f"{warning}\n"
                                self.__warning += 1
        return item_texture, terrain_texture


class module_checker(object):
    def __init__(self):
        self.__status = True
        self.__res_list = []
        self.__manifests = {}
        self.__info = ''

    def get_info(self):
        return self.__info

    def check_module(self):
        base_folder = os.path.join(os.path.dirname(__file__), "modules")
        res_list = []
        for module in os.listdir(base_folder):
            manifest = os.path.join(
                base_folder, module, "module_manifest.json")
            if os.path.exists(manifest) and os.path.isfile(manifest):
                with open(manifest, 'r', encoding='utf8') as f:
                    data = json.load(f)
                name = data['name']
                if name in res_list:
                    self.__status = False
                    self.__info = f'Conflict name {name}.'
                    return False
                else:
                    self.__manifests[name] = data['description']
                    res_list.append(name)
            else:
                self.__status = False
                self.__info = f"Bad module '{module}', no manifest file."
                return False
        self.__status = True
        self.__res_list = res_list
        return True

    def get_module_list(self):
        self.check_module()
        if not self.__status:
            return []
        else:
            return self.__res_list

    def get_manifests(self):
        self.check_module()
        if not self.__status:
            return {}
        else:
            return self.__manifests


def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
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
    main()
