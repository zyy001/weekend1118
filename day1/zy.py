import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("zyy")
driver.find_element_by_id("password").send_keys(123456)
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
driver.find_element_by_css_selector("body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img").click()
time.sleep(5)
cwh=driver.current_window_handle
whs=driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("joinCarButton").click()
time.sleep(5)
driver.find_element_by_css_selector("body > div.shop_last.w1100 > div.other_shopl.fl > div.shopCar_T > span.shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()