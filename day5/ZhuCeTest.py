#有了mytestcase以后,再写测试用例,就不需要重新写setup和teardown方法
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    #因为MyTestCase已经实现了setup和teardown方法,我们以后再写测试用例,就不需要重新实现setup和teardown方法]
    def test_zhu_ce(self):
        """打开注册页面"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        #driver.current_url#用来获取当前浏览器中的网址
        actual=driver.title#用来获取当前浏览器中标签页的title
        expected = '用户登录 - 道e坊商城 - Powered by Haidao'
        base_path = os.path.dirname(__file__)
        path=base_path.replace('day5','report/image')
        driver.get_screenshot_as_file(path + 'zhuce.png')
        self.assertEqual(actual,expected)