import ctypes

#imagepath = r"C:\Users\Jordon\Pictures\test.jpg"

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\Jordon\Pictures\Mario.bmp", 0)
SPIF_UPDATEINIFILE = 0x2
