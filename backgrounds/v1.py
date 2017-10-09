import os
import time
from winreg import *

mor_path = 'C:\\backgrounds\morning.bmp'
day_path = 'C:\\backgrounds\day.bmp'
nig_path = 'C:\\backgrounds\\night.bmp'


def change_desk(picpath):
    key = CreateKey(HKEY_CURRENT_USER, "Control Panel\Desktop")
    SetValueEx(key, "Wallpaper", 0, REG_SZ, picpath)
    CloseKey(key)
    os.system('RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters')


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
