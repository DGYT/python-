import os
import time
from winreg import *

mor_path = 'C:\\backgrounds\morning.exe'
day_path = 'C:\\backgrounds\day.exe'
nig_path = 'C:\\backgrounds\\night.exe'


def change_desk(picpath):
    key = CreateKey(HKEY_CURRENT_USER, "Control Panel\Desktop")
    SetValueEx(key, "Wallpaper", 0, REG_SZ, picpath)
    CloseKey(key)
    os.system(picpath)


def current_hour():
    return time.localtime()[3]


def which_pic(h):
    if 5 <= h < 8:
        return mor_path
    elif 8 <= h < 18:
        return day_path
    else:
        return nig_path


if __name__ == '__main__':
    h = current_hour()
    pic_path = which_pic(h)
    change_desk(pic_path)
