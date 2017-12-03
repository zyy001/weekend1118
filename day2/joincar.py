import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/")
login_link=driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("zyy")
driver.find_element_by_id("password").send_keys(123456)
driver.find_element_by_id("username") .submit()
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
iphone_link=" div.protect_con > div > div.shop_01-imgbox > a "
iphone=driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name('address[address_name]').send_keys("可可")
driver.find_element_by_name('address[mobile]').send_keys(15612121005)
# driver.find_element_by_id("add-new-area-select").find_element_by_css_selector('[value="230000"]').click()
# driver.find_element_by_css_selector('[value="230700"]').click()
# driver.find_element_by_css_selector('[value="230704"]').click()

sheng=driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value('230000')
shi=driver.find_elements_by_tag_name('select')[1]
Select(shi).select_by_value('230700')
qu=driver.find_elements_by_tag_name('select')[2]
Select(qu).select_by_index(2)
# Select(qu).select_by_visible_text('伊春区')
# Select(qu).
# driver.find_element_by_class_name("add-new-name-span-2").send_keys(";lkjdfgggg")
# driver.find_element_by_class_name('add-new-name-span-3').send_keys('111111')
# driver.find_element_by_class_name('aui_state_highlight').click()