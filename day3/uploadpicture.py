# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://localhost/index.php?m=admin&c=public&a=login')
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('userpass').send_keys('password')
driver.find_element_by_name('userverify').send_keys('1234')
driver.find_element_by_class_name("Btn").click()
# 2.商品管理
driver.find_element_by_css_selector("body > div.header > div.menu-box > div.menu.fl > a:nth-child(2)").click()
# 3.添加商品
driver.find_element_by_link_text('添加商品').click()
# 4.商品名称
driver.switch_to.frame('mainFrame')
driver.find_element_by_name('name').send_keys('华为1')
# 5.商品的分类
driver.find_element_by_id('1').click()
driver.find_element_by_id('2').click()
driver.find_element_by_id('6').click()
ActionChains(driver).double_click(driver.find_element_by_id('7')).perform()
# driver.find_element_by_id('7').click()
# driver.find_element_by_id('jiafen').click()
# 6.商品品牌
driver.find_element_by_css_selector('[value="1"]').click()
#7.点击商品图册
driver.find_element_by_link_text('商品图册').click()

#有些页面控件是javascript在页面加载之后生成的,implicitily_wait是用来判断整个网页是否加载完毕的,有时页面加载完,但是javascript的控件还没有创建好,所以需要time.sleep()来提高程序的稳定性
time.sleep(3)
#因为真正负责上传文件的页面元素是<input type="file"....,所以我们可以直接操作这个控件,这个控件可以直接输入图片的路径
driver.find_element_by_name('file').send_keys('D:/upload.png')
#点击开始上传,同时用三个class定位,中间用点号隔开
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
time.sleep(3)
driver.switch_to.alert.accept()
#页面太长点击不了下面的按钮,怎么操作滚动条,range是区间,默认从0开始,到长度-1结束,range(10)表示0到9,一共10个数字,
#拖动滚动条向下
ac = ActionChains(driver)
for i in range(10):
    ac.send_keys(Keys.ARROW_DOWN)
ac.perform()
# 7.提交
driver.find_element_by_class_name('button_search').click()
