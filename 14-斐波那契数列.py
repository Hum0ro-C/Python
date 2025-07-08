"""
题目：斐波那契数列

version：1.0.0
Author: Hum0ro

"""

n = int(input("请输入要输出的项数："))
a, b = 1, 1
for _ in range(n):
    print(a , end=' ')
    a , b = b, a + b 
