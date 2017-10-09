必须放在c盘下，把整个backgrounds文件夹，因为*.exe里的地址是写死的

# ================v1================

RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters

这个参数用来更新桌面，但是win7下有时不能更新。需要试试别的方法



# ================v2================

使用这个方法来更新桌面：
SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\backgrounds\\morning.bmp", SPIF_SENDCHANGE);

使用了点c++，生成exe文件，再用python调用。写死了，不太好。但是ctypes没搞懂，怎么传c++类型的参数。


# ================v3================

RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters

继续用v1的更新桌面方法，但是不用必须放在c盘下了。只要放在一个文件夹就可以了。
