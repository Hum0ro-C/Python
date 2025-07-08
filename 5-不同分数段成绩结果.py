"""
题目：不同的分数段获得不同成绩

version：1.0.0
Author: Hum0ro
"""

score = float(input("请输入分数："))

if 90 <= score <= 100:
    reslut = "您的成绩为：优秀"

elif 80 <= score < 90:
    reslut = "您的成绩为：良好"

elif 70 <= score < 80:
    reslut = "您的成绩为：中等"

elif 60 <= score < 70:
    reslut = "您的成绩为：一般"
elif 0 <= score < 60:
    reslut = "您的成绩不及格，再接再厉" 
else:
    reslut = "您的成绩无效！请重新输入！"

print(reslut)
