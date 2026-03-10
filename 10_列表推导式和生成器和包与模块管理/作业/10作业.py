

# 1.实现万年历效果图，使用函数封装:
#   A:先输出提示语句，并接受用户输入的年、月。
#   B:根据用户输入的年，先判断是否是闰年。
#   C:根据用户输入的月来判断月的天数。
#   D:用循环计算用户输入的年份距1900年1月1日的总天数。
#   E:用循环计算用户输入的月份距输入的年份的1月1日共有多少天,
#   F:相加D与E的天数，得到总天数。
#   G:用总天数来计算输入月的第一天的星期数
#   H:根据G的值，格式化输出这个月的日历!

def get_canlendar():
    #A:先输出提示语句，并接受用户输入的年、月。
    input_year = int(input("请输入年份："))
    input_month = int(input("请输入月份："))
    get_print(input_year, input_month)


def get_year(year) -> bool:
    # B:根据用户输入的年，先判断是否是闰年。
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days(month, year):
    # C:根据用户输入的月来判断月的天数。
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if get_year(year):
            return 29
        else:
            return 28
    return 0

def get_total_days_in_year(year):
    # D:用循环计算用户输入的年份距1900年1月1日的总天数。
    total_days = 0
    for i in range(1900, year):
        total_days += 366 if get_year(i) else 365
    return total_days

def get_total_days_in_month(month, year):
    # E:用循环计算用户输入的月份距输入的年份的1月1日共有多少天。
    total_days = 0
    for i in range(1, month):
        total_days += get_days(i, year)
    return total_days

def total_days(month, year):
    # F:相加D与E的天数，得到总天数。
    return get_total_days_in_year(year) + get_total_days_in_month(month, year)

def get_week_day(month, year):
    # G:用总天数来计算输入月的第一天的星期数。
    return total_days(month, year) % 7

def get_print(year, month):
    week = get_week_day(month, year)
    # H:根据G的值，格式化输出这个月的日历!
    print(f"{year}年{month}月的日历:")
    print("一", "二", "三", "四", "五", "六", "日", sep=" ")
    for i in range(week):
        print("  ", end=" ")  # 打印空格,下方格式day:2d为两位，所以空格也要两位占位，间隔为1个空格
    for day in range(1, get_days(month, year) + 1):
        print(f"{day:2d}", end=" ")
        if (day + week) % 7 == 0:
            print()
    print()

get_canlendar()

# 2.请写一个生成器函数,生成一个无限序列,从1开始可以不断往后取值,每次+1
#    提示:使用while True, 通过调用n次next来获取前n个数
import time
def fib():
    i = 1
    while True:
        yield i   # 可以当成return理解，但是return只能返回一次并结束，yield可以返回多次
        i += 1
gen = fib()

while True:
    print(next(gen))
    time.sleep(2)