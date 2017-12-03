from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
#从浏览器中所有窗口中排除第一个窗口,剩下第二个窗口
cwh=driver.current_window_handle
whs=driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("username").send_keys("zyy")
driver.find_element_by_id("password").send_keys(123456)
driver.find_element_by_class_name("login_btn").click()