import os
# make sure that the app is being run on windows:
if os.name != "nt":
    print("This only works on windows!")
    exit()


from time import sleep
import win32api
from time import sleep


while True:
    mouse_pos = win32api.GetCursorPos()
    print(mouse_pos)
    sleep(0.1)
    os.system("cls")
    