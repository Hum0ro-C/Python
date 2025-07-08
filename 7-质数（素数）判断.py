
"""
题目：输入一个正整数判断它是不是素数(质数)
素数：只能被 1 和它本身整除的数（1 不是素数）

version：1.0.0
Author: Hum0ro

"""

import math

# 输入一个正整数
num = int(input("请输入一个正整数："))

# 判断是否是素数
def is_prime(n):
    if n < 2:
        return False  # 小于 2 的都不是素数
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 有其他因数，不是素数
    return True

# 输出结果
if is_prime(num):
    print(f"{num} 是素数")
else:
    print(f"{num} 不是素数，请重新输入！")
