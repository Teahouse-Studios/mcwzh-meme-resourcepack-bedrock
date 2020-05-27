import zipfile
import json
import argparse
import os

# GPL 3.0


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
    # build with blue ui textures
    if not args['without_blueui']:
        for file in os.listdir("meme_resourcepack/textures/ui"):
            pack.write("meme_resourcepack/textures/ui/" + file)
    # build with textures
    if not args['without_texture']:
        for file in os.listdir("meme_resourcepack/textures/entity"):
            pack.write("meme_resourcepack/textures/entity/" + file)
        for file in os.listdir("meme_resourcepack/textures/blocks"):
            pack.write("meme_resourcepack/textures/blocks/" + file)
        for file in os.listdir("meme_resourcepack/textures/items"):
            pack.write("meme_resourcepack/textures/items/" + file)
        for file in os.listdir("meme_resourcepack/models/entity"):
            pack.write("meme_resourcepack/models/entity/" + file)
        pack.write("meme_resourcepack/textures/map/map_background.png")
        pack.write("meme_resourcepack/textures/terrain_texture.json")
    pack.close()


def build_all():
    build({'type': 'zip', 'without_texture': False, 'without_blueui': False})
    build({'type': 'zip', 'without_texture': True, 'without_blueui': False})
    build({'type': 'zip', 'without_texture': False, 'without_blueui': True})
    build({'type': 'zip', 'without_texture': True, 'without_blueui': True})
    build({'type': 'mcpack', 'without_texture': False, 'without_blueui': False})
    build({'type': 'mcpack', 'without_texture': True, 'without_blueui': False})
    build({'type': 'mcpack', 'without_texture': False, 'without_blueui': True})
    build({'type': 'mcpack', 'without_texture': True, 'without_blueui': True})


def get_packname(args):
    base_name = "meme_resourcepack"
    if args['without_texture']:
        base_name += "_notexture"
    if args['without_blueui']:
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
    parser.add_argument('-t', '--without-texture', action='store_true',
                        help="Do not add textures when building resource packs. If build type is 'all', this argument will be ignored.")
    parser.add_argument('-u', '--without-blueui', action='store_true',
                        help="Do not add the blue ui textures when building resource packs. If build type is 'all', this argument will be ignored.")
    return parser


if __name__ == '__main__':
    main()
