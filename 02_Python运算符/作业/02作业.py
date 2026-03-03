
# 1. 已知深中通道长度为24KM，小军驾驶的雷米汽车 从大桥深圳端开始平均时速100km/h的速度行驶,  求需要多久可以达到中山？
l = 24
v = 100
t = l / v
print(t)

# 2. 已知从深圳到长沙的总距离是800KM，其中高速有700KM，城市路段有100KM，
#     高速最快可120km/h速度行驶，城市道路最快60km/h行驶, 求最快多久可以到达目的地？
length = 800
length_high = 700
length_city = 100
high_v = 120
city_v = 60
t_high = length_high / high_v
t_city = length_city / city_v
time = t_high + t_city
print(time)

# 3. 华氏温度转摄氏温度
#  【提示：将华氏温度转换为摄氏温度(F是华氏温度)  F = 1.8C + 32】
F = float(input("请输入华氏温度："))
C = F - 32 / 1.8
print(f"摄氏温度为：{C:.2f}")

# 4, 小红刚入职一家企业月薪10K，合同期3年，老板同意每年给他涨幅入职薪水的20%，
#       问合同到期后小红的工资是多少？此时老板催促续签合同，如果你是小红 是否会继续待在公司?
salary = 10 + 10 * 0.2 * 2
print(f"合同到期工资为{salary:.2f}K")

# 5, 为抵抗洪水，战士连续作战89小时，编程计算共多少天零多少小时？
hours = 89
days = hours // 24
hours = hours % 24
print(f"共{days}天{hours}小时")

# 6, 给定一个5位数，分别把这个数字的万位，千位，百位、十位、个位算出来并显示。如： 12345
#    提示： 可以使用运算符整除// 和 求余%
num = int(input("请输入5位数："))
w = num // 10000
q = num // 1000 % 10
b = num // 100 % 10
s = num // 10 % 10
g = num % 10
print(f"万位：{w}, 千位：{q}, 百位：{b}, 十位：{s}, 个位：{g}")

# 7. BMI（身体质量指数）的计算公式为BMI=体重（千克）/身高的平方（米）
#   请输入您的身高 和 体重，计算BMI值，判断是否在18.5~25之间？
higght = float(input("请输入您的身高（单位m）："))
weight = float(input("请输入您的体重（单位kg）："))
BMI = weight / higght ** 2
if 18.5 <= BMI <= 25:
    print(f"BMI值为{BMI:.2f}，在18.5~25之间")
else:
    print(f"BMI值为{BMI:.2f}，不在18.5~25之间")


