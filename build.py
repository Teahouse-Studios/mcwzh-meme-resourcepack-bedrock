import zipfile
import json
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description="Automatically build bedrock add-ons")
    parser.add_argument('type', default='zip',
                        help="Build type. Should be 'all', 'zip' or 'mcpack'.")
    args = vars(parser.parse_args())
    if args['type'] == 'all':
        build_all()
    else:
        build(args)
    print("Build succeeded!")


def build(args):
    pack_name = "meme_resourcepack"
    if args['type'] == 'zip':
        # zip rename
        pack_name = pack_name + ".zip"
    elif args['type'] == 'mcpack':
        # mcpack rename
        pack_name = pack_name + ".mcpack"
    # all builds have these files
    pack = zipfile.ZipFile(pack_name, 'w', compression=zipfile.ZIP_DEFLATED)
    pack.write("LICENSE")
    pack.write("meme_resourcepack/pack_icon.png")
    pack.write("meme_resourcepack/manifest.json")
    pack.write("meme_resourcepack/texts/zh_ME.lang")
    pack.write("meme_resourcepack/texts/languages.json")
    pack.write("meme_resourcepack/texts/language_names.json")
    pack.close()


def build_all():
    build({'type': 'zip'})
    build({'type': 'mcpack'})


if __name__ == '__main__':
    main()
