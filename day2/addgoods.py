# 1.登录
from selenium import webdriver
from selenium.webdriver import ActionChains

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
driver.find_element_by_name('name').send_keys('华为')
# 5.商品的分类
driver.find_element_by_id('1').click()
driver.find_element_by_id('2').click()
driver.find_element_by_id('6').click()
ActionChains(driver).double_click(driver.find_element_by_id('7')).perform()
# driver.find_element_by_id('7').click()
# driver.find_element_by_id('jiafen').click()
# 6.商品品牌
driver.find_element_by_css_selector('[value="1"]').click()
# 7.提交
driver.find_element_by_class_name('button_search').click()