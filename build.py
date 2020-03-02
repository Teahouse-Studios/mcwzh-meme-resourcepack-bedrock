import zipfile
import json
import argparse
import os

# Thanks to MysticNebula70

def main():
    parser = argparse.ArgumentParser(
        description="Automatically build bedrock add-ons")
    parser.add_argument('type', default='zip',
                        help="Build type. Should be 'all', 'zip' or 'mcpack'.")
    parser.add_argument('-n', '--without-texture', action='store_true',
                        help="Do not add textures when building resource packs. If build type is 'all', this argument will be ignored.")
    args = vars(parser.parse_args())
    if args['type'] == 'all':
        build_all()
    else:
        build(args)
    print("Build succeeded!")


def build(args):
    pack_name = get_packname(args)
    # all builds have these files
    pack = zipfile.ZipFile(pack_name, 'w', compression=zipfile.ZIP_DEFLATED)
    pack.write("LICENSE")
    pack.write("meme_resourcepack/pack_icon.png")
    pack.write("meme_resourcepack/manifest.json")
    for file in os.listdir("meme_resourcepack/texts"):
            pack.write("meme_resourcepack/texts/" + file)
    # build with textures
    if not args['without_texture']:
        for file in os.listdir("meme_resourcepack/textures/environment"):
            pack.write("meme_resourcepack/textures/environment/" + file)
        for file in os.listdir("meme_resourcepack/textures/ui"):
            pack.write("meme_resourcepack/textures/ui/" + file)
        pack.write("meme_resourcepack/textures/painting/kz.png")
    pack.close()


def build_all():
    build({'type': 'zip', 'without_texture': False})
    build({'type': 'zip', 'without_texture': True})
    build({'type': 'mcpack', 'without_texture': False})
    build({'type': 'mcpack', 'without_texture': True})


def get_packname(args):
    base_name = "meme_resourcepack"
    if args['type'] == 'zip':
        if args['without_texture']:
            base_name = base_name + "_notexture"
            return base_name + ".zip"
        elif not args['without_texture']:
            return base_name + ".zip"
    elif args['type'] == 'mcpack':
        if args['without_texture']:
            base_name = base_name + "_notexture"
            return base_name + ".mcpack"
        elif not args['without_texture']:
            return base_name + ".mcpack"


if __name__ == '__main__':
    main()
