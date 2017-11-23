import os
import time

while 1:
    time.sleep(60)
    status = os.system('tasklist|findstr "Thunder.exe"')
    with open("log", 'a') as f:
        f.write('tasklist|findstr "Thunder.exe"  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n')
    if 1 == status:
        os.system('taskkill /f /t /im "ThunderPlatform.exe"')
        with open("log", 'a') as f:
            f.write(
                'taskkill /f /t /im "ThunderPlatform.exe"   ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n')
        time.sleep(600)
