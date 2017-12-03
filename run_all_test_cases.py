import unittest


if __name__ == '__main__':
    #defaultTestLoader默认的测试用例加载器,用于寻找符合一定规则的测试用例,discover是发现的意思
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    unittest.TextTestRunner().run(suite)