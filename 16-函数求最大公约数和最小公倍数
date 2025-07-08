"""
题目：使用函数计算求最大公约数和最小公倍数

version：1.0.0
Author: Hum0ro

"""

x = int(input("请输入x的整数："))
y = int(input("请输入y的整数："))

def gcd(x,y):
    if x > y:
        x,y = y,x
    for f in range(x,0,-1):
        if x % f == 0 and y % f == 0:
            return f

def lcm(x,y):
    return x*y //gcd(x,y)

print(f'{x,y}的最大公约数为：',gcd(x,y))
print(f'{x,y}的最小公倍数为：',lcm(x,y))
