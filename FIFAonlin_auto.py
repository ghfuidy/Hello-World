import win32gui
import win32api, win32con
import time
import random
from PIL import Image, ImageGrab
import pywinio
import atexit
import threading


def get_window_info():  # 获取阴阳师窗口信息
    wdname = u'FIFA ONLINE 4'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '小轩提示：请打开PC端阴阳师\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        win32gui.SetForegroundWindow(handle)
        win_rect = win32gui.GetWindowRect(handle)
        if win_rect[0] < 0:
            win32api.SendMessage(handle,win32con.WM_SYSCOMMAND,win32con.SC_RESTORE,0)
            win_rect = win32gui.GetWindowRect(handle)
        else:
            pass
        return win_rect


def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

def get_posx(x, screen_size):  # 返回x相对坐标
    return screen_size[0] * x / 1600


def get_posy(y, screen_size):  # 返回y相对坐标
    return screen_size[1] * y / 900

                            
def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b

#键盘程序

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

__winio = None

def __get_winio():
    global __winio

    if __winio is None:
            __winio = pywinio.WinIO()
            def __clear_winio():
                    global __winio
                    __winio = None
            atexit.register(__clear_winio)

    return __winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte( KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80)

def key_press(scancode, press_time = 0.2):
    key_down( scancode )
    time.sleep( press_time )
    key_up( scancode )

# 测试
window_size = get_window_info()
print(window_size)
screensize = [1280,720]
print(resolution())
time.sleep(1)


one_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\one.png')
one_img_hash = get_hash(one_img)
two_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\two.png')
two_img_hash = get_hash(two_img)
finial_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\finial.png')
finial_img_hash = get_hash(finial_img)
skip_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\S_skip.png')
skip_img_hash = get_hash(skip_img)
over_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\over.png')
over_img_hash = get_hash(over_img)
confirm_img = Image.open(r'D:\python_example\helloworld_python\HTML\FIFA_img\confirm.png')
confirm_img_hash = get_hash(confirm_img)

topx, topy = window_size[0], window_size[1]

def first_grab():
    first_img = ImageGrab.grab((topx + get_posx(1240, screensize), topy + get_posy(810, screensize),
                            topx + get_posx(1400, screensize), topy + get_posy(840, screensize)))
    now_img_hash = get_hash(first_img)
    test = hamming(one_img_hash,now_img_hash)
    return test

def two_grab():
    two_img = ImageGrab.grab((topx + get_posx(1240, screensize), topy + get_posy(870, screensize),
                                topx + get_posx(1400, screensize), topy + get_posy(910, screensize)))
    now_img_hash = get_hash(two_img)
    test = hamming(two_img_hash,now_img_hash)
    return test

def finial_grab():
    two_img = ImageGrab.grab((topx + get_posx(1243, screensize), topy + get_posy(873, screensize),
                                topx + get_posx(1403, screensize), topy + get_posy(907, screensize)))
    now_img_hash = get_hash(two_img)
    test = hamming(finial_img_hash,now_img_hash)
    return test

def skip_grab():
    img = ImageGrab.grab((topx + get_posx(1480, screensize), topy + get_posy(875, screensize),
                                topx + get_posx(1505, screensize), topy + get_posy(900, screensize)))
    now_img_hash = get_hash(img)
    test = hamming(skip_img_hash,now_img_hash)
    img_end = ImageGrab.grab((topx + get_posx(760, screensize), topy + get_posy(215, screensize),
                                topx + get_posx(850, screensize), topy + get_posy(250, screensize)))
    img_end_hash = get_hash(img_end)
    end_test = hamming(over_img_hash,img_end_hash)
    img_confirm = ImageGrab.grab((topx + get_posx(1235, screensize), topy + get_posy(875, screensize),
                                topx + get_posx(1410, screensize), topy + get_posy(905, screensize)))
    img_confirm_hash = get_hash(img_confirm)
    confirm_test = hamming(confirm_img_hash,img_confirm_hash)
    return test or end_test or confirm_test

#查看图片
def start_game():
    n_time = 2
    # x_time = 1
    while n_time < 100:
        if first_grab():
            key_press(0x39)
            while n_time < 100:
                time.sleep(n_time)
                if two_grab():
                    key_press(0x39)
                    print('ok')
                    time.sleep(n_time*30)
                    while n_time < 100:
                        if finial_grab():
                            key_press(0x39)
                            break
                        else:
                            print('finial error')
                            time.sleep(60)
                    break
                else:
                    print('two error,retry')
            time.sleep(10)
        else:
            print('first error')
            time.sleep(n_time)
            n_time += 1

def S_detect():
    nomean = 1
    while nomean == 1:
        if skip_grab():
            key_press(0x1f)
            print('skip')
            time.sleep(10)
        else:
            print('retry')
            time.sleep(10)
            

t = threading.Thread(target=start_game, name='firstloopThread')
f = threading.Thread(target=S_detect, name='secondloopThread')
t.start()
f.start()
t.join()
f.join()