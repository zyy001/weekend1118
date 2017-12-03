import unittest

import time
from selenium import webdriver


class DengLuTest(unittest.TestCase):
    '''登录模块测试用例'''
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配才能用窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()


    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver
        driver.get('http://localhost/index.php?m=user&c=public&a=login')
        driver.find_element_by_id('username').send_keys('zyy')
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_css_selector('body > div.login_main.w1180.clearfix > div.login.fr > form > ul > li:nth-child(5) > input').click()
        print("当前用户名:zyy")

