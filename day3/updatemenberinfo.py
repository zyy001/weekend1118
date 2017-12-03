#1.登陆
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://localhost/index.php?m=user&c=public&a=login')
driver.find_element_by_id('username').send_keys('zyy')
#链表和数组不同,数组有固定的长度,链表要有明确的结束标志
ActionChains(driver).send_keys(Keys.TAB).send_keys('123456').send_keys(Keys.ENTER).perform()
#2.点击账号设置
driver.find_element_by_link_text('账号设置').click()
#3.点击个人资料
driver.find_element_by_partial_link_text('个人资料').click()
#4.修改个人信息
#clear是清空的意思,用来清除元素中原本的内容,更好的编程习惯,在每次send_keys之前都使用clear清空一下
driver.find_element_by_id('true_name').clear()
driver.find_element_by_id('true_name').send_keys('朱迪')
#选性别,css可以使用多个属性组合定位一个元素,一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector('[value="2"]').click()

#javascript是一个单独语言,和python的语法不一样,不能直接在pycharm中执行
js='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id('date').clear()
driver.find_element_by_id('date').send_keys("2000-01-01")
#也可使用


# date=driver.execute_script("return document.getElementById('date')")
# date.click()

#输入qq号码,点击提交
driver.find_element_by_id('qq').clear()
driver.find_element_by_id('qq').send_keys('123455')
driver.find_element_by_class_name('btn4').click()
#右键检查不了html代码的弹出框,叫做alert,有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的,所以implicitly_wait对这个控件不管用
#切换到alert的方法,和切换窗口的方法类似
#alert弹出框,accept接收,同意,确定,dismiss拒绝,取消
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
