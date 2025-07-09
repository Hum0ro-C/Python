"""
题目：计算指定的年月日是这一年的第几天

version：1.0.0
Author: Hum0ro

"""

import sys

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_year(year, month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29

    if month < 1 or month > 12:
        print('月份无效！程序退出！')
        sys.exit()

    if day < 1 or day > month_days[month - 1]:
        print('日期无效！程序退出！')
        sys.exit()

    return sum(month_days[:month - 1]) + day

def main():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))

    # 月份校验，非法直接退出，不执行后面输入日期
    if month < 1 or month > 12:
        print("月份无效！程序退出！")
        sys.exit()

    day = int(input("请输入日期："))

    # 调用计算函数，内部日期也会校验
    day_number = get_day_of_year(year, month, day)
    print(f"{year}年{month}月{day}日是该年的第 {day_number} 天！")

if __name__ == '__main__':
    main()
