import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.LoginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #
        #1.打开网页
        #self.driver.get('http://localhost/index.php?m=user&c=public&a=login')
        lp = LoginPage(self.driver)  #实例化一个登陆页面
        lp.open()
        #2.输入用户名
        #self.driver.find_element(By.ID,'username').send_keys('zyy')
        lp.input_username('zyy')
        #3.输入密码
        #self .driver.find_element(By.ID,'password').send_keys('123456')
        lp.input_password('123456')
        #4.点击登陆按钮
        #self.driver.find_element(By.CLASS_NAME,'login_btn').click()
        lp.click_login_button()
        #5.验证是否跳转到管理中心页面
        # expected = '我的会员中心 - 道e坊商城 - Powered by Haidao'
        # time.sleep(5)
        # self.assertIn('我的会员中心',self.driver.title)#判断我的页面title中包不包含我的会员中心这几个字
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
    elf.assertEqual(pcp.title,self.driver.title)