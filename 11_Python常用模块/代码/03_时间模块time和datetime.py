import time


# time模块
#   time.time()  # 当前时间
#   time.sleep() # 暂停,休眠, 单位:秒
# 当前时间, 时间戳timestamp:从1970年1月1日0点到现在所经过的秒
# 1s = 1000ms 毫秒
# 1ms = 1000us 微秒
# 1us = 1000ns 纳秒
'''
# 1s = 1000 000 000 ns
# 1s = 1e9  ns
print(1e9) # 1000 000 000.0
'''
print(time.time())  # 1773191097.9006815
time.sleep(2)  # 参数单位是秒



# datetime: 日期时间,
#   对time做了封装,比time更好用
#   date: 日期,表示年月日
#   time: 时间,表示时分秒
import datetime

# 1.创建日期对象
dt = datetime.datetime.now()  # 获取当前时间
print(dt)  # 2026-03-11 09:52:04.030512

dt = datetime.datetime(2026,8,1)
print(dt)  # 2026-08-01 00:00:00

dt = datetime.datetime(2026,8,1,9,30,20)
print(dt)  # 2026-08-01 09:30:20



# 2.日期的属性
print(dt.year,dt.month,dt.day) # 2026 8 1 (年,月,日)
print(dt.hour,dt.minute,dt.second)  # 9 30 20 (时,分,秒)
print(dt.date())  # 2026-08-01 (日期)
print(dt.time())  # 09:30:20 (时间)

print()


# 3. 日期格式的转换
#   日期对象 : datetime对象
#   日期字符串 : "2030-02-01 12:30:20"
#   时间戳 :  1821025084.211286

# 日期对象 <==> 日期字符串
# strftime: 日期对象 => 日期字符串
# strptime: 日期字符串 => 日期对象

dt = datetime.datetime(2026,8,1,9,30,20)
print(dt, type(dt))  # 2026-08-01 09:30:20 <class 'datetime.datetime'>


dt1 = dt.strftime("%Y-%m-%d %H-%M-%S")    # 日期对象 => 日期字符串
print(dt1, type(dt1))  # 2026-08-01 09-30-20 <class 'str'>  

dt2 = dt.strftime("%x %X")
print(dt2, type(dt2))  # 08/01/26 09:30:20 <class 'str'>


s = "2030-02-01 12:30:20"
dt3 = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")   # 日期字符串 => 日期对象
print(dt3, type(dt3))  # 2030-02-01 12:30:20 <class 'datetime.datetime'>

'''
> # %y 两位数的年份表示（00-99）
> # %Y 四位数的年份表示（0000-9999）
> # %m 月份（01-12）
> # %d 月内中的一天（0-31）
> # %H 24小时制小时数（0-23）
> # %I 12小时制小时数（01-12）
> # %M 分钟数（00-59）
> # %S 秒（00-59）

> # %a 本地简化星期名称
> # %A 本地完整星期名称
> # %b 本地简化的月份名称
> # %B 本地完整的月份名称
> # %c 本地相应的日期表示和时间表示
> # %j 年内的一天（001-366）
> # %p 本地A.M.或P.M.的等价符
> # %U 一年中的星期数（00-53）星期天为星期的开始
> # %w 星期（0-6），星期天为星期的开始
> # %W 一年中的星期数（00-53）星期一为星期的开始
> # %x 本地相应的日期表示
> # %X 本地相应的时间表示
> # %% %号本身
'''

print()



# 日期对象 <==> 时间戳 (了解)
# 时间戳本身是一个浮点数, 代表从1970年1月1日0点到现在所经过的秒数, 包含小数部分表示毫秒和微秒

dt = datetime.datetime.now()   
print(dt, type(dt))  # 2026-03-11 10:47:51.479616 <class 'datetime.datetime'>

dt_timestamp = dt.timestamp()   # 日期对象 => 时间戳
print(dt_timestamp, type(dt_timestamp))  # 1773197271.479616 <class 'float'> 

dt = datetime.datetime.fromtimestamp(dt_timestamp)
print(dt, type(dt))  # 2026-03-11 11:06:33.735026 <class 'datetime.datetime'>  (时间戳 => 日期对象)



print()


# 时间差 timedelta
# timedelta: 时间差对象, 表示两个日期之间的差值

# 练习1: 求7天后的日期
d1 = datetime.datetime.now()
print(d1)    # 2026-03-11 11:12:40.947365
td = datetime.timedelta(days=7)
print(td)     # 7 days, 0:00:00
print(d1+td)    # 2026-03-18 11:12:40.947365
print(d1-td)    # 2026-03-04 11:12:40.947365

# 求2个日期相差多少天
d2 = datetime.datetime(2030, 10, 10)
d3 = datetime.datetime(2020, 3, 3)
delta = d2 - d3
print(delta, type(delta))  # 3873 days, 0:00:00 <class 'datetime.timedelta'>
print(delta.days)  # 3873  timedelta对象的days属性表示相差的天数







