from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):#构造方法
        self.driver = driver

    title = '用户登录 - 道e坊商城 - Powered by Haidao'
    url = 'http://localhost/index.php?m=user&c=public&a=login'
#小括号表示元组,元组中有两个值,第一个元素是控件的定位方式,第二个元素是控件定位方式的值
    username_input_loc = (By.ID,'username')
    password_input_loc = (By.ID,'password')
    login_button_loc=(By.CLASS_NAME,'login_btn')
    def open(self):
        self.driver.get(self.url)
    def input_username(self,username):
        #self.driver.find_element_by_id('username').send_keys(username)
        #self.driver.find_element(By.ID,'username').send_keys(username)
    #星号的作用就是把一个元组中的元素分别传入方法参数中,前面一个星号,表示传入的就不是元组,而是元组中的两个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element_by_id('password').send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_class_name('login_btn').click()


