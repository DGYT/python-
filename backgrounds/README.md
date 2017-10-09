必须放在c盘下，把整个backgrounds文件夹，因为*.exe里的地址是写死的

# ================v1================

RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters

这个参数用来更新桌面，但是win7下有时不能更新。需要试试别的方法



# ================v2================

SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\backgrounds\\morning.bmp", SPIF_SENDCHANGE);

使用了点c++，生成exe文件，再用python调用。写死了，不太好。但是ctypes没搞懂，怎么传c++类型的参数。
