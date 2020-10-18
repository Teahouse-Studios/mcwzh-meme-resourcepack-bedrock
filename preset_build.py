if __name__ == '__main__':
    import build
    from os import listdir, mkdir, remove, rename
    from os.path import exists, isdir, join

    preset_args = [
        {'type': 'zip', 'compatible': True, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': ['blue_ui']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {'resource': [
            'a_letter', 'bagify', 'observer_think', 'trident_model']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': True, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'zip', 'compatible': False, 'modules': {
            'resource': ['all']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': ['all']}, 'hash': False, 'output': 'builds'}
    ]
    preset_name = [
        "meme-resourcepack_compatible_noresource_noblueui.zip",
        "meme-resourcepack_noresource_noblueui.mcpack",
        "meme-resourcepack_noresource.mcpack",
        "meme-resourcepack_noblueui.mcpack",
        "meme-resourcepack_compatible_noresource_noblueui.mcpack",
        "meme-resourcepack.zip",
        "meme-resourcepack.mcpack"
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
        pack_name, warning_count, error, _ = build.build(args)
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
    print(
        f"\nBuilt {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")
