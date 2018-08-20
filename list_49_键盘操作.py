import pyautogui, time

# print(pyautogui.size())
# width, height = pyautogui.size()
# print(pyautogui.position())

def mouse_move():
    for i in range(4):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

time.sleep(1)
def Draw_luoquan():
    print(pyautogui.position())

    pyautogui.click()
    distance = 100
    interval = 20
    dur = 0.1

    while distance > 0:
        pyautogui.dragRel(distance, 0, dur)
        distance = distance - interval
        pyautogui.dragRel(0, distance, dur)
        pyautogui.dragRel(-distance, 0, dur)
        distance = distance - interval
        pyautogui.dragRel(0, -distance, dur)

def image_distribute():
    ###图片分辨
    im = pyautogui.screenshot()
    print(im.getpixel((50,200)))

    print(pyautogui.pixelMatchesColor(50, 200, (222, 186, 198, 255)))
    time.sleep(2)
    imageLocation = pyautogui.locateAllOnScreen('we_game.png')

    print(list(imageLocation))


def color_extract():
    print('Press fn+command(Mac) or Ctrl+C(windows) to quit.')
    positionStr = ''
    try:
        while True:
            time.sleep(3)
            x, y = pyautogui.position()
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr = 'X: {:4}  Y: {:4} RGB:{}'.format(x, y, pixelColor)

            print(positionStr)

    except KeyboardInterrupt:
        print('\nDone')

from pynput import mouse
class myException(Exception):
    pass
def on_click(x, y, button, pressed):
    if pressed:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getcolors
        print((x, y)), pixelColor

    if button == mouse.Button.right:
        raise myException(button)

###键盘输入
def jianpanshuru():
    pyautogui.click(100,100)
    time.sleep(2)
    pyautogui.typewrite('Hello world!\n')
    pyautogui.typewrite(['a','b','left','X','Y'], 0.25)
    ###输出全部键值---------------
    print(pyautogui.KEYBOARD_KEYS)
    ###---------------------------
    pyautogui.keyDown('shift')
    pyautogui.press('2')
    pyautogui.keyUp('shift')

    pyautogui.press('#')

    ###组合键------------------------
    pyautogui.click(100, 100)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'right')
    pyautogui.hotkey('ctrl', 'v')
    ###------------------------------




