import unittest
#导入ddt包
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read
#2.装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
#3.调用之前写好的read()方法,获取配置文件中的数据
    member_info=read('member_info.csv')

    #在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print('所有方法之前,只执行一次')
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.close()

    def test_a_log_in(self):
        print('登陆测试用例')
        driver=self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name('username').send_keys('admin')
        ActionChains(driver).send_keys(Keys.TAB).send_keys('password').send_keys(Keys.TAB).send_keys('1234').send_keys(Keys.ENTER).perform()
    #5.@ddt.data()测试数据来源于read()方法
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        #每组测试数据就是一个测试用例,每条测试用例都应该是独立的,所以此处不推荐用for循环
        #4.注释掉for循环,改变代码的缩进,
        # for row in read('member_info.csv'):
        #     print('添加会员')
        driver = self.driver
        driver.find_element_by_link_text('会员管理').click()
        driver.find_element_by_link_text('添加会员').click()
        iframe_css='#mainFrame'
        iframe_html=driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name('username').send_keys('z'+row[0])
        driver.find_element_by_name('mobile_phone').send_keys(row[1])
        driver.find_element_by_css_selector('[value="'+row[2]+'"]').click()
        driver.find_element_by_id('birthday').send_keys(row[3])
        driver.find_element_by_name('email').send_keys(row[4])
        driver.find_element_by_name('qq').send_keys(row[5])
        driver.find_element_by_class_name('button_search').click()
#之前的代码能够自动运行但是不能自动判断程序运行是否正确,actual实际结果,expected期望结果
        actual=driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(1) > div').text
        expected='z'+row[0]
        # if actual==expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")
        #断言叫assert,断言是框架提供的,要想调用断言,必须加上self.因为测试用例继承了框架中的TestCase类,也继承了这个类中的断言,所以我们可以直接用断言方法
        #断言比较简洁,只有错误时才会有提示信息,正确无任何信息,断言报错时,后面的代码将不会继续执行
        self.assertEqual(actual,expected)


        #由于是循环的,输入会员名后再次切换回去上个镶嵌页才能点击会员管理
        #切换到父框架
        driver.switch_to.parent_frame()


if __name__ == '__main__':
    unittest.main()