#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Torre Yang
# datetime:2018/9/9 19:58
from selenium import webdriver
import os
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)


# 浏览器是否打开开关; 0 关浏览器 1 打开浏览器
def chromeDriver(url, type):
    if type == 0:
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
    else:
        driver = webdriver.Chrome()
        driver.get(url)
    logging.info('等待页面加载')
    sleep(3)
    return driver


def firefoxDriver(url):
    option = webdriver.FirefoxOptions()
    option.add_argument("headless")
    driver = webdriver.Firefox(firefox_options=option)
    driver.get(url)
    return driver