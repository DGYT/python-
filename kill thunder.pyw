import os
import time

with open("log", 'a') as f:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')

while 1:
    time.sleep(60)
    status = os.system('tasklist|findstr "Thunder.exe"')
    if 1 == status:
        os.system('taskkill /f /t /im "ThunderPlatform.exe"')
        time.sleep(600)
