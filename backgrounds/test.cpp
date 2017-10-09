#include <windows.h>

void main()
{
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\backgrounds\\morning.bmp", SPIF_SENDCHANGE);
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\backgrounds\\morning.bmp", SPIF_SENDCHANGE);
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\backgrounds\\morning.bmp", SPIF_SENDCHANGE);
    
}
