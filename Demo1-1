"""

编写一个程序，输入一个年份，判断是否为闰年。是闰年则输出 True，否则输出 False。
闰年的判断规则如下：
普通闰年：能被 4 整除但不能被 100 整除；
世纪闰年：能被 400 整除。

version：1.0
Author: Hum0ro

"""

while True:
    year = int(input("请输入年份（输入 0 退出）："))
    
    if year == 0:
        print("程序结束。")
        break  # 退出循环

    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    print(f"{year} 是闰年吗？{is_leap}")
