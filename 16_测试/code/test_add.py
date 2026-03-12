import unittest

# 测试文件要引入被测试的函数和类
from add import my_add


# 创建类，以Test开头，表示这是一个用于测试的类
# 继承父类unittest.TestCase，可以使用父类的各种测试功能

class TestMyAdd(unittest.TestCase):

    # 在此测试下定义不同测试用例，每个测试用例都是测试类下面的一个方法
    # 所有测试方法必须test_开头，unittest库会自动搜索该开头的方法当成测试用例

    def test_positive_with_positive(self):

        # assert：（不建议）
        # 一旦出现AssertionError，程序中断，后续测试用例无法执行
        # assert my_add(5, 6) == 8

        # unittest.TestCase 里的类方法（推荐）
        # 测试类直接继承该类，可以通过self调用父类方法
        # 被测试函数和类为参数传入
        # self.assertEqual(my_add(5, 6), 8)   # AssertionError: 11 != 8
        self.assertEqual(my_add(5, 6), 8)
        print("test_positive_with_positive被执行了")

    def test_negative_with_positive(self):
        self.assertEqual(my_add(-5, 6), 1)
        print("test_negative_with_positive被执行了")

# 使用 python test_add.py 
# 直接运行测试文件需要在测试程序末尾加上这一段
if __name__ == '__main__':
    unittest.main()


# 使用 python -m unittest
# 不需要 if __name__ == '__main__': unittest.main()