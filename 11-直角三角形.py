"""
题目：打印直角三角形
*
**
***
****
*****

version：1.0.0
Author: Hum0ro

"""

row = int(input("请输入一个整数："))

if row == 1:
    print("*")  # 直接打印一颗星
else:
    for i in range(1, row + 1):
        print("*" * i)

