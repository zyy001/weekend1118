from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("注册").click()
cwh=driver.current_window_handle
whs=driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_name("username").send_keys("zyy1")
driver.find_element_by_name("password").send_keys(123456)
driver.find_element_by_name("userpassword2").send_keys(123456)
driver.find_element_by_name("mobile_phone").send_keys(15212122005)
driver.find_element_by_name("email").send_keys("147852@qq.com")
driver.find_element_by_class_name("reg_btn").click()