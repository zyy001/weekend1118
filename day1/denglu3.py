from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("zyy")
driver.find_element_by_id("password").send_keys(123456)
driver.find_element_by_class_name("login_btn").click()