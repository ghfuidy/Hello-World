from time import sleep
from subprocess import call
import subprocess
import os
import uiautomator
from cv2 import cv2 as cv2
from PIL import Image
import numpy as np

def screencap(name):
    call('adb shell screencap /sdcard/{}.png'.format(name))
    call("adb pull /sdcard/{}.png D:\\".format(name))
    sleep(5)

def circle():
    call('adb shell input swipe {} {} {} {}'.format(880,1170,880,150))
    sleep(30)
    call('adb shell input keyevent 4')

def imgdiffer(temurl):
    # im1 = Image.open(r'D:\\explor.png')
    # im1.save(r'D:\\explor.png')
    target = cv2.imread("D:\\twenty.png")
    template = cv2.imread(temurl)
    theight, twidth = template.shape[:2]
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    # cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val)
    return min_loc[0]+twidth/2,min_loc[1]+theight/2,min_val

def searchimg():
    screencap('twenty')
    width_2,height_2,match_val_2 = imgdiffer("D:\\visit.png")
    width_1,height_1,match_val_1 = imgdiffer("D:\\explore.png")
    if match_val_1 < match_val_2:
        width = width_1
        height = height_1
        match_val = match_val_1
    else:
        width = width_2
        height = height_2
        match_val = match_val_2
    return width, height, match_val

def taobao():
    # subprocess.Popen('adb shell am start -n com.taobao.taobao/com.taobao.tao.TBMainActivity',shell=True, stdout=subprocess.PIPE)
    # call('adb shell input tap {} {}'.format(752,1300))
    # sleep(10)
    # print("event is finish")
    # call('adb shell input tap {} {}'.format(912,1707))
    # sleep(10)
    # print("renwu is finish")
    match_val = 0
    while match_val < 0.03:
        width,height,match_val = searchimg()
        if match_val >= 0.03:
            print('no match target')
            call('adb shell input swipe {} {} {} {}'.format(405,1536,405,1000))
            width,height,match_val = searchimg()
        if match_val < 0.03:
            call('adb shell input tap {} {}'.format(width,height))
            print("tap")
            sleep(10)
            for i in range(1,10,1):
                call('adb shell input swipe {} {} {} {}'.format(880,1170,880,150))
                sleep(2)
            sleep(5)
            call('adb shell input keyevent 4')
            print('wipe is finish')
            sleep(3)
        else:
            break

def uiandroid():
    from uiautomator import Device

    d = Device('192.168.1.100:5555')
    print(d.info)



if __name__ == '__main__':
    # res = subprocess.Popen('adb devices',shell=True, stdout=subprocess.PIPE)
    # res.stdout.read()
    # call('adb tcpip 5555')
    # call('adb connect 192.168.1.100')
    # call('adb devices')
    # sleep(10)
    # call('adb shell input keyevent 26')
    # subprocess.Popen('adb shell input tap {} {}'.format(220,170),shell=True, stdout=subprocess.PIPE)
    # 打开淘宝，淘宝日常
    taobao()
    # #另一种自动化方式
    # uiandroid()
    #打开小米
    # subprocess.Popen('adb shell am start -n com.xiaomi.shop/com.xiaomi.shop2.activity.MainActivity',shell=True, stdout=subprocess.PIPE)
    # # screencap('miaosha')
    # call('adb shell input tap {} {}'.format(546,1144))
    # print("hello world")