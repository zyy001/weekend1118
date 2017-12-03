#1.导入unittest框架
import unittest
#python中的类名和文件名可以一样,但是推荐:文件名首字母小写,类名首字母大写,其余一样
#2.继承unittest中的父类,python中的继承直接用小括号表示,TestCase是测试用例的意思
class UnittestDemo(unittest.TestCase):
    #3.重写父类中的方法setUp(创建的意思),def是方法的关键字
    def setUp(self):
        print("这个方法将会在测试用例执行前执行")
    def tearDown(self):
        print('这个方法将在测试用例执行后执行')
    #4.编写测试用例方法,只有以test开头的方法才是测试用例方法,测试用例方法可以直接被运行.普通方法不能直接运行,只有被调用才能执行
    def test_log_in(self):
        print('登录测试用例')
        self.zhu_ce()
    def zhu_ce(self):
        print('注册测试用例')
    def test_search(self):
        print('搜索测试用例')
#如果你直接执行这个文件,那么就会直接执行下面的语句
#否则,你执行其他文件时,import这个文件的时候下面的语句就不会执行
if __name__ == '__main__':
    #执行当前文件中所有的unittest的测试用例
    unittest.main()
