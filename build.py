import zipfile
import json
import argparse
import os

# Apache 2.0


def main():
    parser = generate_parser()
    args = vars(parser.parse_args())
    if args['type'] == 'clean':
        for i in os.listdir('builds/'):
            os.remove('builds/' + i)
        print("Deleted all packs built.")
    else:
        if args['type'] == 'all':
            build_all()
        else:
            build(args)
        print("Build succeeded!")


def build(args: dict) -> None:
    pack_name = "builds/" + get_packname(args)
    # check build path
    if os.path.exists("builds"):
        if not os.path.isdir("builds"):
            os.remove("builds")
            os.mkdir("builds")
    else:
        os.mkdir("builds")
    # all builds have these files
    pack = zipfile.ZipFile(
        pack_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5)
    pack.write("LICENSE")
    pack.write("meme_resourcepack/pack_icon.png")
    pack.write("meme_resourcepack/manifest.json")
    for file in os.listdir("meme_resourcepack/texts"):
        pack.write("meme_resourcepack/texts/" + file)
    pack.write("meme_resourcepack/textures/map/map_background.png")
    # get all modified textures
    textures = get_texture_list(args['include'])
    # process list
    (files, item_texture, terrain_texture) = process_list(textures)
    # write to pack
    for file in files:
        arcname = "meme_resourcepack/" + file[file.find(os.sep, 8)+1:]
        pack.write(file, arcname)
    if item_texture:
        pack.writestr("meme_resourcepack/textures/item_texture.json",
                      json.dumps(item_texture, indent=4))
    if terrain_texture:
        pack.writestr("meme_resourcepack/textures/terrain_texture.json",
                      json.dumps(terrain_texture, indent=4))
    pack.close()


def build_all():
    build({'type': 'zip', 'include': ['all']})
    build({'type': 'zip', 'include': ['none']})
    build({'type': 'zip', 'include': ['blue_ui']})
    build({'type': 'zip', 'include': [
          'bagify', 'observer_think', 'ore_highlight', 'trident_model']})
    build({'type': 'mcpack', 'include': ['all']})
    build({'type': 'mcpack', 'include': ['none']})
    build({'type': 'mcpack', 'include': ['blue_ui']})
    build({'type': 'mcpack', 'include': [
          'bagify', 'observer_think', 'ore_highlight', 'trident_model']})


def get_packname(args: dict) -> str:
    base_name = "meme_resourcepack"
    if 'none' in args['include']:
        base_name += "_notexture"
    if 'all' in args['include']:
        pass
    elif not 'blue_ui' in args['include']:
        base_name += "_noblueui"
    if args['type'] == 'zip':
        return base_name + ".zip"
    elif args['type'] == 'mcpack':
        return base_name + ".mcpack"


def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Automatically build add-ons")
    parser.add_argument('type', default='zip',
                        help="Build type. Should be 'all', 'zip', 'mcpack' or 'clean'. If it's 'clean', all packs in 'builds/' directory will be deleted.",
                        choices=['all', 'zip', 'mcpack', 'clean'])
    parser.add_argument('-i', '--include', nargs='*', default='all',
                        help="(Experimental) Include modification folders. Should be path(s) to a folder, 'all' or 'none'(currently does not support a single file). Defaults to 'all'.")
    return parser


def get_texture_list(texture_list: list) -> set:
    textures = set()
    if 'none' in texture_list:
        pass
    elif 'all' in texture_list:
        textures.update("optional/" + path for path in os.listdir('optional'))
    else:
        for path in texture_list:
            if os.path.exists('optional/' + path):
                textures.add('optional/' + path)
            else:
                print(
                    f'\033[33m[WARN] "{path}" does not exist, skipping\033[0m')
    return textures


def process_list(texture_list: set) -> (set, dict, dict):
    items = []
    terrains = []
    file_list = set()
    for item in texture_list:
        base = item[item.rfind(os.sep)+1:]
        for root, dirs, files in os.walk(item):
            for file in files:
                if file == 'item_texture.json':
                    items.append(os.path.join(root, file))
                elif file == 'terrain_texture.json':
                    terrains.append(os.path.join(root, file))
                else:
                    file_list.add(os.path.join(root, file))
    item_texture = merge_json_to_dict(items)
    terrain_textures = merge_json_to_dict(terrains)
    return file_list, item_texture, terrain_textures


def merge_json_to_dict(files: list) -> dict:
    result = {'texture_data': {}}
    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            content = json.load(f)
        result['texture_data'].update(content['texture_data'])
    return result


if __name__ == '__main__':
    main()
