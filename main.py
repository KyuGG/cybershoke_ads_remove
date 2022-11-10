# file manipulations
from os import listdir, remove, system
from shutil import copyfile

# colored console
from colorama import Fore

# keyboard events
from pynput.keyboard import Key, Listener

# handle csgo path
from src.get_csgo_path import get_csgo_path


def print_menu(chosen_line):
    system('cls')
    print(f'{Fore.BLUE}cybershoke ads remove{Fore.RESET}')
    for index, line in enumerate(MENU):
        line = f'{Fore.MAGENTA}{line} <--{Fore.RESET}' if chosen_line == index else line
        print(line)
    print(f'{Fore.BLUE}press ESC to exit{Fore.RESET}')


def change_chosen_line(chosen_line):
    global current_chosen_line
    if chosen_line > len(MENU) - 1:
        current_chosen_line = 0
    elif chosen_line < 0:
        current_chosen_line = len(MENU) - 1
    else:
        current_chosen_line = chosen_line


def main(chosen_line, csgo_path):
    option = bool(chosen_line)

    overlay = '/csgo/materials/overlay/'
    overlay_path = csgo_path + overlay
    overlay_files = listdir(overlay_path)

    is_hud_exists = False

    for file in overlay_files:
        if file.startswith('cybershoke') and file.endswith('.vtf'):
            is_hud_exists = True
            if option:
                copyfile('hud/cybershoke.vtf', overlay_path + file)
            else:
                remove(overlay_path + file)

    if is_hud_exists:
        print(f'{Fore.GREEN}success!{Fore.RESET}')
    else:
        print(f'{Fore.RED}HUD file doesn\'t exist,\njoin server to download it{Fore.RESET}')



def on_press(key):
    global current_chosen_line
    match key:
        case Key.up:
            current_chosen_line -= 1
        case Key.down:
            current_chosen_line += 1
        case Key.enter:
            main(current_chosen_line, csgo_path)
            return
        case Key.esc:
            return False
        case _:
            return

    change_chosen_line(current_chosen_line)
    print_menu(current_chosen_line)


MENU = (
    '0. Get default HUD back',
    '1. Remove ads from HUD',
)

current_chosen_line = 0

csgo_path = get_csgo_path()

if 'error' in csgo_path.keys():
    print(f'{Fore.RED}{csgo_path.get("error")}{Fore.RESET}')
    exit()

csgo_path = csgo_path.get('path')

print_menu(current_chosen_line)


with Listener(on_press=on_press, suppress=True) as listener:
    listener.join()
