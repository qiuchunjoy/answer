# -*- coding: GB2312 -*-
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

from nose.tools import *
# from pymouse import PyMouse

import unittest
# 导入操作系统相关命令的
# import linux system commond
import os
# 导入生成HTML格式测试报告的HtmlTestRunner包
# import HTML format test reports packages
import HtmlTestRunner
# 导入删除文件用的shutil包
# import handle files packages
import shutil
# import pyautogui

'''
github:
xxxxxxx.com

brif introduction:
1.install appium related software, i wrote a introduction docments already, read it first please
2.according to scripts below to run codes or use vertical or horizon XYZ to locate elements
3.update htmltestrunner source code to get the test report you need
'''


delList = []
delDir = "D:\\python\\taskOne\\newpic"
delList = os.listdir(delDir)

# 执行用例测试前，清空截图文件夹下的图片
# before run test cases, empty screenshot folder's files
for f in delList:
    filePath = os.path.join(delDir, f)
    if os.path.isfile(filePath):
        os.remove(filePath)
        print
        filePath + " was removed!"
    elif os.path.isdir(filePath):
        shutil.rmtree(filePath, True)
    print
    "Directory: " + filePath + " was removed!"


# 这个类将在下面作为装饰器使用
# decorator
class take_screen_shot():
    def __init__(self, func):
        self.func = func
        # 拼接截图文件名
        # concate screenshot names
        self.name = func.__name__ + ' (__main__.taskOneTestCases).png'
        # 对每次调用的函数都做截图操作
        # take screenshot every step

    def __call__(self, *args):
        try:
            self.func(self, *args)
        finally:
            # 定义截图路径，并将截图保存其中
            # define screenshot dir, and maintain screenshot inside it
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'D:\\python\\taskOne\\newpic')
            file_path = os.path.join(path, self.name)
            driver.get_screenshot_as_file(file_path)


class taskOneTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设置操作平台 set env
        desired_caps['platformVersion'] = '5.0.1'  # 操作系统版本 set system version
        desired_caps['deviceName'] = '6&c8cec40&0&0001'  # 设备名称 device name

        desired_caps['appPackage'] = 'net.crypto.taskOne'
        desired_caps['appActivity'] = 'net.crypto.view.login.LoginActivity'
        global driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @take_screen_shot  # 对每一条测试用例使用装饰器 | take screenshot before execute each test case
    def test__01_login(self):
        # 检查是否已安装 | check wether already install app software
        driver.is_app_installed('net.crypto.taskOne')
        # 等待activity加载 | wait activity load
        driver.wait_activity("net.crypto.view.login.LoginActivity", 50, 1)
        # 定义鼠标触摸事件action | define mouse touch action
        action = TouchAction(driver)
        # 定义移动鼠标事件action | define mouse move action
        action1 = ActionChains(driver)
        # 根据左上角三条横线的ID进行点击操作 | click button on top left side 
        driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_account")').click()
        # 根据跳转页面的9-Day Forecast ID进行点击操作 | click 9-Day forecast page
        driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_pwd")').click()
        # 或是根据相对坐标点击也可以
    @classmethod
    def tearDownClass(self):
        driver.quit()  # 退出当前应用 quit
if __name__ == '__main__':  # 下面语句用来生成测试报告 get test reports
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='cal_report', descriptions='hello', report_title='crypto weather 测试报告'))