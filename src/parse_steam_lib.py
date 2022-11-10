import vdf


def parse_steam_lib(path):
    with open(f'{path}/config/libraryfolders.vdf', encoding='utf-8') as file:
        steam_libraries = vdf.load(file).get('libraryfolders')

    steam_libraries_parsed = []
    for index in range(len(steam_libraries)):
        steam_library = steam_libraries[str(index)]
        # fmt: off
        steam_library_parsed = {
            'path': steam_library.get('path'),
            'apps': steam_library.get('apps')
        }
        # fmt: on
        steam_libraries_parsed.append(steam_library_parsed)
    return steam_libraries_parsed
