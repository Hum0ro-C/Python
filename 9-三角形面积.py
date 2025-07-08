"""
题目：海伦公式计算三角形面积

    一般三角形：周长 = 边长a + 边长b + 边长c。
    等腰三角形：周长 = 2a + b（a为腰长，b为底边长）。
    等边三角形：周长 = 3a（a为任一一边的长度）。

version：1.0.0
Author: Hum0ro

"""

import math

# 获取用户输入的三条边
a = float(input("请输入第一条边长："))
b = float(input("请输入第二条边长："))
c = float(input("请输入第三条边长："))

# 判断是否构成三角形
if a + b > c and a + c > b and b + c > a:

# 计算三角形的周长   
    s = a + b + c 

# 计算三角形的面积 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'可以构成一个三角形,面积为：{area:.2f}')
else:
    print("不能构成三角形 ❌")
