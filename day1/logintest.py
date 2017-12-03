#1.打开浏览器
from selenium import webdriver
driver=webdriver.Chrome()
#2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3.输入用户名

# driver.find_element_by_id("username").send_keys("zyy")
# driver.find_element_by_id("password").send_keys(123456)
# driver.find_element_by_class_name("login_btn").click()

#4.输入密码
#5.点击登陆按钮