from json import load
from os import listdir, mkdir, remove, rename
from os.path import exists, isdir, join
from sys import exit
from memepack_builder.wrapper import main as _main

PACK_VERSION = '1.3.5'


def check_version_consistency():
    manifest = load(
        open("meme_resourcepack/manifest.json", 'r', encoding='utf8'))
    header_version = '.'.join(str(i)
                              for i in manifest['header']['version'])
    modules_version = '.'.join(str(i)
                               for i in manifest['modules'][0]['version'])
    return PACK_VERSION == header_version and PACK_VERSION == modules_version


def main():
    if check_version_consistency():
        preset_args = [
            {'platform': 'be', 'type': 'mcpack', 'compatible': False, 'modules': {
                'resource': ['all'], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'mcpack', 'compatible': False, 'modules': {
                'resource': ['blue_ui'], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'mcpack', 'compatible': False, 'modules': {'resource': [
                'minecart_helmet', 'spicy_strips'], 'collection': ['no_blue_ui']}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'mcpack', 'compatible': False, 'modules': {
                'resource': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'mcpack', 'compatible': True, 'modules': {
                'resource': ['all'], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'mcpack', 'compatible': True, 'modules': {
                'resource': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'zip', 'compatible': False, 'modules': {
                'resource': ['all'], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'platform': 'be', 'type': 'zip', 'compatible': True, 'modules': {
                'resource': [], 'collection': []}, 'hash': False, 'output': 'builds'},
        ]
        preset_name = [
            f"meme-resourcepack_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_noresource_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_noblueui_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_noresource_noblueui_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_compatible_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_compatible_noresource_noblueui_v{PACK_VERSION}.mcpack",
            f"meme-resourcepack_v{PACK_VERSION}.zip",
            f"meme-resourcepack_compatible_noresource_noblueui_v{PACK_VERSION}.zip",
        ]
        pack_counter = 0
        perfect_pack_counter = 0
        base_folder = "builds"
        build_unsuccessful = 0
        if exists(base_folder) and not isdir(base_folder):
            remove(base_folder)
        if not exists(base_folder):
            mkdir(base_folder)
        for file in listdir(base_folder):
            remove(join(base_folder, file))
        for args, name in zip(preset_args, preset_name):
            result = _main(args, True)
            if result['error_code'] == 0:
                pack_counter += 1
                if result['warning_count'] == 0:
                    perfect_pack_counter += 1
                if name != "meme-resourcepack.zip" and name != "meme-resourcepack.mcpack":
                    rename(join(base_folder, result['file_name']),
                           join(base_folder, name))
                    print(f"Renamed pack to {name}.")
            else:
                print(f"Failed to build pack {name}.")
                build_unsuccessful = 1
        print(
            f"\nBuilt {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")
        exit(build_unsuccessful)
    else:
        exit(
            f'\033[1;31mError: Pack version "{PACK_VERSION}" does not match number in manifest.json.\033[0m')


if __name__ == '__main__':
    main()
