'''
Created on 2018年7月19日

@author: Admin
'''
#! /usr/bin/env python
#coding=utf-8
import os
import time
from appium import webdriver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android' #设备系统
desired_caps['platformVersion'] = '7.0'#设备系统版本
desired_caps['deviceName'] = '58Y0217C03001231'#设备名称
# desired_caps['app'] = PATH('G:\\QQ\\920525654\\FileRecv\\app-debug (3).apk')
desired_caps['appPackage'] = 'com.rr.rrsdkdemo'
desired_caps['appActivity'] = 'com.rr.rrsdkdemo.MainActivity'

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  #启动app

time.sleep(5)  #启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
driver.find_element_by_id('com.rr.rrsdkdemo:id/bt_login').click()

driver.quit()