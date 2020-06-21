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


def build(args):
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
    # build with blue ui textures
    if not args['without_blueui']:
        for file in os.listdir("meme_resourcepack/textures/ui"):
            pack.write("meme_resourcepack/textures/ui/" + file)
    # build with textures
    if not args['without_texture']:
        for file in os.listdir("meme_resourcepack/textures/bagify"):
            pack.write("meme_resourcepack/textures/bagify/" + file)
        for file in os.listdir("meme_resourcepack/textures/observer_think"):
            pack.write("meme_resourcepack/textures/observer_think/" + file)
        for file in os.listdir("meme_resourcepack/textures/ore_highlight"):
            pack.write("meme_resourcepack/textures/ore_highlight/" + file)
        for file in os.listdir("meme_resourcepack/textures/trident_model"):
            pack.write("meme_resourcepack/textures/trident_model/" + file)
        pack.write("meme_resourcepack/entity/thrown_trident.entity.json")
        pack.write("meme_resourcepack/textures/terrain_texture.json")
        pack.write("meme_resourcepack/textures/item_texture.json")
    pack.close()


def build_all():
    build({'type': 'zip', 'include': ['all']})
    build({'type': 'zip', 'include': ['none']})
    build({'type': 'zip', 'include': ['blue_ui']})
    build({'type': 'zip', 'include': [
          'bagify', 'observer_think', 'ore_hightlight', 'trident_model']})
    build({'type': 'mcpack', 'include': ['all']})
    build({'type': 'mcpack', 'include': ['none']})
    build({'type': 'mcpack', 'include': ['blue_ui']})
    build({'type': 'mcpack', 'include': [
          'bagify', 'observer_think', 'ore_hightlight', 'trident_model']})


def get_packname(args):
    base_name = "meme_resourcepack"
    if 'none' in args['include']:
        base_name += "_notexture"
    if not 'blue_ui' in args['include']:
        base_name += "_noblueui"
    if args['type'] == 'zip':
        return base_name + ".zip"
    elif args['type'] == 'mcpack':
        return base_name + ".mcpack"


def generate_parser():
    parser = argparse.ArgumentParser(
        description="Automatically build add-ons")
    parser.add_argument('type', default='zip',
                        help="Build type. Should be 'all', 'zip', 'mcpack' or 'clean'. If it's 'clean', all packs in 'builds/' directory will be deleted.",
                        choices=['all', 'zip', 'mcpack', 'clean'])
    parser.add_argument('-i', '--include', nargs='*', default='all',
                        help="(Experimental) Include modification strings or folders. Should be path(s) to a file, folder, 'all' or 'none'. Defaults to 'all'.")
    return parser

def get_texture_list(texture_list):
    textures = set()
    if 'none' in texture_list:
        pass
    elif 'all' in texture_list:
        textures.update("optional/" + file for file in os.listdir('optional'))
    else:
        for path in texture_list:
            if os.path.exists(path):
                if os.path.isfile(path):
                    textures.add(path)
                elif os.path.isdir(path):
                    textures.add()



def merge_json(base_file, merge_file):
    with open(base_file, 'r', encoding='utf8') as b:
        base_data = json.load(b)
    with open(merge_file, 'r', encoding='utf8') as m:
        merge_data = json.load(m)
    base_data.update(merge_data)
    with open(base_file, 'w', encoding='utf8') as f:
        json.dump(base_data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
