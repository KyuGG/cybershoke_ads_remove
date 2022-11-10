from src.get_steam_path import get_steam_path
from src.parse_steam_lib import parse_steam_lib


def get_csgo_path():
    STEAM_PATH = get_steam_path()
    if STEAM_PATH == None:
        return {'error': 'Steam doesn\'t exist'}

    steam_libraries_parsed = parse_steam_lib(STEAM_PATH)
    csgo_path: str = ''
    for steam_library in steam_libraries_parsed:
        if '730' in steam_library.get('apps').keys():
            csgo_path = steam_library.get('path')
            break

    if not csgo_path:
        return {'error': 'CS:GO doesn\'t exist'}

    csgo_path += '/steamapps/common/Counter-Strike Global Offensive'
    return {'path': csgo_path}
