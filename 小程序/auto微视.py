from time import sleep
from subprocess import call
import subprocess
import os
# import uiautomator


def weishi():
    """
    腾讯微视自动浏览拿宝箱
    """
    for i in range(1,100,1):
        call('adb shell input swipe {} {} {} {}'.format(405,1536,405,1000))
        print("swipe")
        sleep(10)


def xianyu():
    """
    咸鱼活动，浏览商品拿宝箱
    """
    for i in range(1,100,1):
        call('adb shell input swipe {} {} {} {}'.format(405,1536,405,1000))
        sleep(0.5)
        call('adb shell input tap {} {}'.format(912,1707))
        print("swipe")
        sleep(5)
        call('adb shell input keyevent 4')


# xianyu()
weishi()