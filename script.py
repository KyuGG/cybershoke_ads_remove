from json import load
from os import listdir
from shutil import copyfile
from sys import platform

with open('settings.json') as settings:
    csgo_path = load(settings)
csgo_path = csgo_path.get('csgo_path')

overlay = '/csgo/materials/overlay/' if platform == 'linux' else '\csgo\materials\overlay\\'
overlay_path = csgo_path + overlay
overlay_files = listdir(overlay_path)
for file in overlay_files:
    if file.startswith('cybershoke') and file.endswith('.vtf'):
        copyfile('cybershoke.vtf', overlay_path + file)

input('Скрипт выполнен. Нажмите ENTER')
