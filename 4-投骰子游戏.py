"""
题目：投骰子决定需要做的事情
提示：1英寸(in) = 2.54厘米(cm)

version：1.0.0
Author: Hum0ro
"""
from random import randint

num = randint(1,6)
value = num

print("您的骰子点数为：",value)

if num == 1:
    print("我正在吃饭 🍚")
elif num == 2:
    print("我正在打游戏 🎮")
elif num == 3:
    print("我正在睡觉 🛌")
elif num == 4:
    print("我正在学习 📚")
elif num == 5:
    print("我正在写代码 💻")
elif num == 6:
   print("我正在谈恋爱 ❤️")

