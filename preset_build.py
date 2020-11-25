if __name__ == '__main__':
    import build
    from json import load
    from os import listdir, mkdir, remove, rename
    from os.path import exists, isdir, join
    from sys import exit

    pack_version = '1.1.0'
    build_unsuccessful = 0

    def check_version_consistency():
        manifest = load(
            open("meme_resourcepack/manifest.json", 'r', encoding='utf8'))
        header_version = '.'.join(str(i)
                                  for i in manifest['header']['version'])
        modules_version = '.'.join(str(i)
                                   for i in manifest['modules'][0]['version'])
        return pack_version == header_version and pack_version == modules_version

    if check_version_consistency():
        preset_args = [
            {'type': 'mcpack', 'compatible': False, 'modules': {'language': [], 'resource': [
                'all'], 'mixed': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'type': 'mcpack', 'compatible': False, 'modules': {'language': [], 'resource': [
                'blue_ui'], 'mixed': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'type': 'mcpack', 'compatible': False, 'modules': {'language': [], 'resource': [
            ], 'mixed': [], 'collection': ['no_blue_ui']}, 'hash': False, 'output': 'builds'},
            {'type': 'mcpack', 'compatible': False, 'modules': {'language': [], 'resource': [
            ], 'mixed': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'type': 'mcpack', 'compatible': True, 'modules': {'language': [], 'resource': [
            ], 'mixed': [], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'type': 'zip', 'compatible': False, 'modules': {'language': [], 'resource': [
                'all'], 'mixed':[], 'collection': []}, 'hash': False, 'output': 'builds'},
            {'type': 'zip', 'compatible': True, 'modules': {'language': [], 'resource': [
            ], 'mixed':[], 'collection': []}, 'hash': False, 'output': 'builds'},
        ]
        preset_name = [
            f"meme-resourcepack_v{pack_version}.mcpack",
            f"meme-resourcepack_noresource_v{pack_version}.mcpack",
            f"meme-resourcepack_noblueui_v{pack_version}.mcpack",
            f"meme-resourcepack_noresource_noblueui_v{pack_version}.mcpack",
            f"meme-resourcepack_compatible_noresource_noblueui_v{pack_version}.mcpack",
            f"meme-resourcepack_v{pack_version}.zip",
            f"meme-resourcepack_compatible_noresource_noblueui_v{pack_version}.zip",
        ]
        pack_counter = 0
        perfect_pack_counter = 0
        base_folder = "builds"
        if exists(base_folder) and not isdir(base_folder):
            remove(base_folder)
        if not exists(base_folder):
            mkdir(base_folder)
        for file in listdir(base_folder):
            remove(join(base_folder, file))
        for args, name in zip(preset_args, preset_name):
            pack_name, warning_count, error = build.build(args)
            if not error:
                pack_counter += 1
                if warning_count == 0:
                    perfect_pack_counter += 1
                if name != "meme-resourcepack.zip" and name != "meme-resourcepack.mcpack":
                    rename(join(base_folder, pack_name),
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
            f'\033[1;31mError: Pack version "{pack_version}" does not match number in manifest.json.\033[0m')
