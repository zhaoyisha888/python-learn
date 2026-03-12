#  bug 虫子
> 计算机领域表示程序错误
> **关键**：写出bug后要快速直接的发现

# 测试

## 1. 目的：

>    - 新写的程序行为是否与预期相同
>    - 改动旧代码后，验证其他功能依然按照预期执行

## 2. 如何测试

**方法1**： **assert** 断言

    后面可以跟随任何布尔表达式
    测试时在assert后面跟上我们认为应该为Ture的表达式
        - 表达式为Ture，无事发生，继续执行
        - 表达式为False，抛出AssertionError，程序终止

**方法2**：**unittest** 单元测试库

    单元测试库：对软件中的最小可执行单元进行验证。

    unittest库 为python自带，使用时候直接导入测试程序即可
        - 一次性跑多个测试用例
        - 直观展示哪些用例通过
        

## 3. 写测试

> -  划分测试代码和实现代码, 测试代码放到**test_xxx**的独立文件里
> -  以下创建实现代码`add.py`和测试代码`test_add.py`
>
> **实现代码文件my_add.py**
>
>   ```python
>   # 加法运算实现程序
>   def my_add(x, y):
>       return x + y
>   ```
>
> **测试代码文件test_add.py**
> ```python
>
> import unittest
>
> # 测试文件要引入被测试的函数和类
> from add import my_add
>
>
> # 创建类，以Test开头，表示这是一个用于测试的类
> # 继承父类unittest.TestCase，可以使用父类的各种测试功能
>
> class TestMyAdd(unittest.TestCase):
>
>     # 在此测试下定义不同测试用例，每个测试用例都是测试类下面的一个方法
>     # 所有测试方法必须test_开头，unittest库会自动搜索该开头的方法当成测试用例
>
>     def test_positive_with_positive(self):
>
>         # assert：（不建议）
>         # 一旦出现AssertionError，程序中断，后续测试用例无法执行
>         # assert my_add(5, 6) == 8
>
>         # unittest.TestCase 里的类方法（推荐）
>         # 测试类直接继承该类，可以通过self调用父类方法
>         # 被测试函数和类为参数传入
>         # self.assertEqual(my_add(5, 6), 8)   # AssertionError: 11 != 8
>         self.assertEqual(my_add(5, 6), 8)
>         print("test_positive_with_positive被执行了")
>
>     def test_negative_with_positive(self):
>         self.assertEqual(my_add(-5, 6), 1)
>         print("test_negative_with_positive被执行了")
> ```

## 4. 运行测试

>   - 必须在测试程序所在的路径启动测试运行器
>   
>   - unittest自动自动扫描发现并运行类中所有以 test_ 开头的方法
>   
>   - **注意**：运行有两种命令
>
> ```python
> # 1. 使用 python test_add.py 
> #    直接运行测试文件需要在测试程序末尾加上这一段
> if __name__ == '__main__':
>     unittest.main()
>
>
> # 2. 使用 python -m unittest
> #    不需要 if __name__ == '__main__': unittest.main()
> ```

## 5. 测试结果

> 打开终端，输入以下命令 "python -m unittest", 可以看到终端输出：
> 
>   ```bash
>   PS D:\code\python-learn\16_测试\code> python -m unittest
>   test_negative_with_positive被执行了
>   .F
>   ===================================================================
>   FAIL: test_positive_with_positive (test_add.TestMyAdd.test_positive_with_positive)
>   -------------------------------------------------------------------
>   Traceback (most recent call last):
>     File "D:\code\python-learn\16_测试\code\test_add.py", line 25, in test_positive_with_positive
>       self.assertEqual(my_add(5, 6), 8)
>   AssertionError: 11 != 8
>
>   -------------------------------------------------------------------
>   Ran 2 tests in 0.001s
>
>   FAILED (failures=1)
>   ```

>    - **.F**  ：首个个执行的测试输出.成功，后面一个测试输出F没通过
>    - **AssertionError: 11 != 8**  ：告诉用户测试没通过的原因是什么
>    - **Ran 2 tests in 0.001s** ：显示说明一共执行了两个测试用例
>    - **FAILED (failures=1)**  ：有一个测试用例失败了
>
>    - **test_negative_with_positive被执行了** ：这涉及到测试用例顺序，
>    - 后面执行的测试用例`test_positive_with_positive`错误，所以没有执行后一句打印语句


## 6. 测试用例顺序

> **注意**：**测试的执行顺序不按照代码的书写顺序，而是按照方法名的字母顺序**
>
>    test_negative_with_positive（以 'n' 开头）
>    test_positive_with_positive（以 'p' 开头）
>    因为 'n' 在字母顺序上小于 'p'，所以 test_negative_with_positive 会先执行。

> **控制执行**：最简单的方法就是更改命名方式
> ```python
> def test_1_positive_with_positive(self):  # 先执行
>     self.assertEqual(my_add(5, 6), 11)
>
> def test_2_negative_with_positive(self):  # 后执行
>     self.assertEqual(my_add(-5, 6), 1)
> ```

> **重要原则**:
>   1. 测试应该相互独立，不应该依赖执行顺序。一个好的测试应该：
>   2. 不依赖于其他测试的执行结果
>   3. 可以以任意顺序运行，每次运行结果一致
>   虽然可以控制执行顺序，但最好设计成不依赖顺序的测试。

## unittest.TestCase 类

### 1. 常用测试方法
> **unittest.TestCase** 类提供了一些用于测试的方法，常用的有：
> |        方法名               |         描述           |             示例               |   
> |:--------------------------:|:----------------------:|:------------------------------:|                        
> |1. **assertEqual(a, b)**：   |    检查 a 是否等于 b。  |       **assert a == b**        |
> |2. **assertNotEqual(a, b)**：|    检查 a 是否不等于 b。|      **assert a != b**         |
> |3. **assertTrue(x)**：       |    检查 x 是否为真。    |     **assert bool(x) is True** |
> |4. **assertFalse(x)**：      |    检查 x 是否为假。    |    **assert bool(x) is False** |
> |5. **assertIs(a, b)**：      |    检查 a 是否是 b。    |      **assert a is b**         |
> |6. **assertIsNot(a, b)**：   |    检查 a 是否不是 b。  |     **assert a is not b**      |
> |7. **assertIn(a, b)**：      |    检查 a 是否在 b 中。 |      **assert a in b**         |
> |8. **assertNotIn(a, b)**：   |    检查 a 是否不在 b 中。|   **assert a not in b**       |
>
>
> **注意**：
>   1. 这些方法会在测试失败时抛出 AssertionError 异常。
>   2. 测试方法的命名必须以 test_ 开头，这样 unittest 才能识别它们为测试方法。
>   3. 可以使用 **setUp()** 和 tearDown() 方法来在每个测试方法前后执行一些准备和清理工作。

### 2. setUp()方法
> **setUp()** 方法是 unittest.TestCase 类中的一个方法，用于在每个测试方法执行前进行一些准备工作。
>
> **setUp()** 方法的作用是：
> 1. 在每个测试用例执行前，自动调用 setUp() 方法。
> 2. 可以在 setUp() 方法中执行一些初始化操作，例如创建测试对象、设置测试环境等。
> 3. setUp() 方法是可选的，可以根据需要重写。
>
> **为什么要使用 setUp() 方法？**
> 1. 避免重复代码：每个测试方法互相独立，测试时要分别重复创建测试对象、设置测试环境等
> 2. 可以将这些准备工作放在 setUp() 方法中，然后在每个测试方法中调用 setUp() 方法即可。
> 
> 比如：
> 
> 创建实现代码`sentence.py`
> ```python
> class Sentence(unittest.TestCase):
>     def __init__(self, sentence):
>         self.sentence = sentence
>
>     # 返回句子字母数量
>     def count_letter(self):
>         return len(self.sentence)
>
>     # 返回句子单词数量
>     def count_word(self):
>         return len(self.sentence.split(" "))
>
>     # 返回所有字母大写后的句子
>     def upper(self):
>         return self.sentence.upper()
> ```
>
> 创建测试代码`test_sentence.py`
> 
> ```python
> import unittest
> from sentence import Sentence
>
> class TestSentence(unittest.TestCase):
>     def test_count_letter(self):
>         sentence = Sentence("hello world")
>         self.assertEqual(sentence.count_letter(), 12)
>
>     def test_count_word(self):
>         sentence = Sentence("hello world")
>         self.assertEqual(sentence.count_word(), 2)    
>  
>     def test_upper(self):
>         sentence = Sentence("hello world")
>         self.assertEqual(sentence.upper(), "HELLO WORLD")
> ``` 
> 
> **可以看到**：每个测试方法都需要创建一个 Sentence 对象，这是重复的代码。
>     
> 使用 **setUp()** 方法优化测试代码`test_sentence.py`
> 
> ```python
> import unittest
> from sentence import Sentence
>
> class TestSentence(unittest.TestCase)
>     def setUp(self):
>         self.sentence = Sentence("hello world")
> 
>     def test_count_letter(self)：
>         self.assertEqual(self.sentence.count_letter(), 12):
> 
>     def test_count_word(self)：
>         self.assertEqual(self.sentence.count_word(), 2):
>
>     def test_upper(self)：
>         self.assertEqual(self.sentence.upper(), "HELLO WORLD")
> ```
>
> **可以看到**：每个测试方法都不需要创建 Sentence 对象，而是直接使用 self.sentence。
> 这样可以避免重复代码，提高测试效率。
> 注意：setUp() 方法是可选的，可以根据需要重写。
> 
> 
> 
> 