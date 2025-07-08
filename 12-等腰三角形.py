"""
题目：打印等腰三角形
    *
   ***
  *****
 *******
*********

version：1.0.0
Author: Hum0ro

"""

row = int(input("请输入行数（正整数）："))

if row < 1:
    print("请输入大于 0 的整数")
else:
    max_num = 2 * row - 1  # 最后一行的星号数量

    for i in range(row):
        row_num = i + 1
        star_num = row_num * 2 - 1  # 当前行星号数量
        space = (max_num - star_num) // 2  # 左右空格数量

        print(" " * space + "*" * star_num)
