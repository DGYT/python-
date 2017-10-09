import os
import time
from winreg import *

script_dir = os.path.dirname(__file__)

mor_path = script_dir + "/morning.bmp"
day_path = script_dir + "/day.bmp"
nig_path = script_dir + "/night.bmp"


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
