"""
题目：输入圆的半径计算计算周长和面积
周长公式：2p*r
面积公式：p*r*

version：1.0.0
Author: Hum0ro
"""
# 导入数学模块
import math  

r = float(input("请输入圆的半径："))
circumference = math.pi * 2 * r
area = math.pi * r * r

print(f"半径为 {r} 的圆周长为：{circumference:.2f}")
print(f"半径为 {r} 的圆面积为：{area:.2f}")
