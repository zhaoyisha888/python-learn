
import unittest
from try_setup import Shopping

# 创建一个测试类，以Test开头，表示这是一个用于测试的类
class TestShopping(unittest.TestCase):
    # 在每个测试方法执行前都会执行setUp方法，用于初始化测试环境/对象
    def setUp(self):
        # 这里我们创建一个Shopping对象，用于测试
        self.shopping = Shopping({"牙刷": 10, "毛巾": 15, "水杯": 20})

    def test_get_item_count(self):
        # 测试get_item_count方法
        self.assertEqual(self.shopping.get_item_count(), 3)

    def test_get_total_price(self):
        # 测试get_total_price方法
        self.assertEqual(self.shopping.get_total_price(), 45)


# 使用 python test_try_setup.py 运行测试文件
# 需要加上这一段
if __name__ == '__main__':
    unittest.main()

# 运行结果：说明测试通过
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''