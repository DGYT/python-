import os
import time

while 1:
    # time.sleep(60)
    status1 = os.system('tasklist|findstr "Thunder.exe"')
    with open("log", 'a') as f:
        f.write(
            'tasklist|findstr "Thunder.exe" status:' + str(status1) + ' ' + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime()) + '\n')
    if 1 == status1:
        status2 = os.system('taskkill /f /t /im "ThunderPlatform.exe"')
        # time.sleep(100)
        with open("log", 'a') as f:
            f.write(
                'taskkill /f /t /im "ThunderPlatform.exe" status:' + str(status2) + ' ' + time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
            # time.sleep(600)
