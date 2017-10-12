import os
import time
from ctypes import *
from winreg import *

dir = os.getcwd()
mor_path = dir + '\morning.bmp'
day_path = dir + '\day.bmp'
nig_path = dir + '\\night.bmp'


def change_desk(picpath):
    key = CreateKey(HKEY_CURRENT_USER, "Control Panel\Desktop")
    SetValueEx(key, "Wallpaper", 0, REG_SZ, picpath)
    CloseKey(key)
    change(picpath)


def change(picpath):
    lib = windll.LoadLibrary('USER32.DLL')
    lib.SystemParametersInfoW(0x0014, 0, picpath, 0x0002);


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
    while 1:
        h = current_hour()
        pic_path = which_pic(h)
        change_desk(pic_path)
        time.sleep(1)