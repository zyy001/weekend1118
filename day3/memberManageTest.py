import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    def setUp(self):
        #打开浏览器,driver声明在setUp之内,不能被其他方法访问
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        time.sleep(20)
        self.driver.quit()
    def test_add_member(self):
        driver=self.driver
        driver.get('http://localhost/index.php?m=admin&c=public&a=login')
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('userpass').send_keys('password')
        driver.find_element_by_name('userverify').send_keys('1234')
        driver.find_element_by_class_name("Btn").click()
        driver.find_element_by_link_text('会员管理').click()
        driver.find_element_by_link_text('添加会员').click()
        driver.switch_to.frame('mainFrame')
        driver.find_element_by_name('username').send_keys('zyy1')
        driver.find_element_by_name('mobile_phone').send_keys('13512121005')
        driver.find_element_by_id('birthday').send_keys('2000-11-07')
        driver.find_element_by_name('email').send_keys('24551236@qq.com')
        driver.find_element_by_name('qq').send_keys('355664163')
        driver.find_element_by_class_name('button_search').click()
