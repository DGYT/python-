import os
import time
while 1:
    time.sleep(60)
    status = os.system('tasklist|findstr "Thunder.exe"')
    if 1 == status:
        os.system('taskkill /f /t /im "ThunderPlatform.exe"')
        time.sleep(600)