from json import load
from os import listdir, remove
from shutil import copyfile

with open('settings.json') as settings:
    csgo_path = load(settings)
csgo_path = csgo_path.get('csgo_path')

overlay_path = csgo_path + '\csgo\materials\overlay\\'
overlay_files = listdir(overlay_path)
vtf_names = []
for file in overlay_files:
    if file.endswith('.vtf'):
        vtf_names.append(file)
        remove(overlay_path + file)

for vtf_name in vtf_names:
    copyfile('cybershoke.vtf', overlay_path + vtf_name)

input('Скрипт выполнен. Нажмите ENTER')