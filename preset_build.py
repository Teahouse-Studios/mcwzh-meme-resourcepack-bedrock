import build
import os


if __name__ == '__main__':
    preset_args = [
        {'type': 'zip', 'compatible': False, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'zip', 'compatible': False, 'modules': {
            'resource': ['blue_ui']}, 'hash': False, 'output': 'builds'},
        {'type': 'zip', 'compatible': False, 'modules': {'resource': [
            'a_letter', 'bagify', 'observer_think', 'trident_model']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': ['blue_ui']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {'resource': [
            'a_letter', 'bagify', 'observer_think', 'trident_model']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': True, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'zip', 'compatible': True, 'modules': {
            'resource': []}, 'hash': False, 'output': 'builds'},
        {'type': 'zip', 'compatible': False, 'modules': {
            'resource': ['all']}, 'hash': False, 'output': 'builds'},
        {'type': 'mcpack', 'compatible': False, 'modules': {
            'resource': ['all']}, 'hash': False, 'output': 'builds'}
    ]
    preset_name = [
        "meme-resourcepack_noresource_noblueui.zip",
        "meme-resourcepack_noresource.zip",
        "meme-resourcepack_noblueui.zip",
        "meme-resourcepack_noresource_noblueui.mcpack",
        "meme-resourcepack_noresource.mcpack",
        "meme-resourcepack_noblueui.mcpack",
        "meme-resourcepack_noresource_noblueui_compat.mcpack",
        "meme-resourcepack_noresource_noblueui_compat.zip",
        "meme-resourcepack.zip",
        "meme-resourcepack.mcpack"
    ]
    pack_counter = 0
    perfect_pack_counter = 0
    base_folder = "builds"
    if os.path.exists(base_folder) and not os.path.isdir(base_folder):
        os.remove(base_folder)
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)
    for file in os.listdir(base_folder):
        os.remove(os.path.join(base_folder, file))
    for args, name in zip(preset_args, preset_name):
        pack_name, warning_count, error, _ = build.build(args)
        if not error:
            pack_counter += 1
            if warning_count == 0:
                perfect_pack_counter += 1
            if name != "meme-resourcepack.zip" and name != "meme-resourcepack.mcpack":
                os.rename(os.path.join(base_folder, pack_name),
                          os.path.join(base_folder, name))
                print(f"Renamed pack to {name}.")
        else:
            print(f"Failed to build pack {name}.")
    print(
        f"\nBuilt {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")
