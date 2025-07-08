
"""
题目：英寸和厘米之间的转换
提示：1英寸(in) = 2.54厘米(cm)

version：1.0.0
Author: Hum0ro
"""

length = float(input('请输入长度：'))
value = input('请输入单位（cm/厘米 或 in/英寸）：')

if value == "cm" or value == "厘米":
    value_result = length / 2.54
    print(f'{length:.2f} 厘米 = {value_result:.2f} 英寸')

elif value == "in" or value == "英寸":
    value_result = length * 2.54
    print(f'{length:.2f} 英寸 = {value_result:.2f} 厘米')

else:
    print(" 您输入的单位无效，请输入 cm、厘米、in 或 英寸。")
