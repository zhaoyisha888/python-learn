
class Shopping :
    # 初始化购物清单，shopping_list为字典类型，包含商品和对应价格
    # 例子：{"牙刷"：10，"毛巾"：15，"水杯"：20}
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    # 返回购物清单上有多少种商品
    def get_item_count(self):
        return len(self.shopping_list)

    # 返回购物清单上所有商品的总价
    def get_total_price(self):
        return sum(self.shopping_list.values())

# 这里只是类的声明，并没有实例化对象
# 实例化对象后，才能调用类中的方法和属性
# 我们将在test_02_try_setup.py中实例化对象并调用方法和属性进行测试