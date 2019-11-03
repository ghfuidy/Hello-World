import win32gui
import win32api
import win32con
import time
import threading


def mouselisten():
    mouse_pos = win32gui.GetCursorPos()
    win_Hd = win32gui.WindowFromPoint(mouse_pos)
    print(win_Hd)


t = threading.Thread(target=mouselisten, name='firstloopThread')
t.start()
# t.join()
