from json import load
from os import listdir, remove, system
from shutil import copyfile
from sys import platform


option = input('0. Вернуть обычный HUD\n1. Убрать рекламу из HUD\n')
while option != '0' and option != '1':
    system('cls')
    print('0. Вернуть обычный HUD\n1. Убрать рекламу из HUD')
    print('Несуществующий пункт, повторите ввод')
    option = input()

option = bool(int(option))

with open('settings.json') as settings:
    csgo_path = load(settings)
csgo_path = csgo_path.get('csgo_path')

overlay = '/csgo/materials/overlay/' if platform == 'linux' else '\csgo\materials\overlay\\'
overlay_path = csgo_path + overlay
overlay_files = listdir(overlay_path)

is_hud_exists = False

for file in overlay_files:
    if file.startswith('cybershoke') and file.endswith('.vtf'):
        is_hud_exists = True
        if option:
            copyfile('cybershoke.vtf', overlay_path + file)
        else:
            remove(overlay_path + file)

if not is_hud_exists:
    print('Файл HUD не найден, зайдите на сервер,\nчтобы он был скачан')
else:
    print('Скрипт выполнен')

input('Нажмите ENTER для завершения работы...')
