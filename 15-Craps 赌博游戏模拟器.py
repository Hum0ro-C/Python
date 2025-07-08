"""
题目：Craps 赌博游戏模拟器

version：1.0.0
Author: Hum0ro

"""

import random

money = 1000  # 初始资金

print("🎲 欢迎来到 Craps 赌博游戏！你有1000元启动资金。")

while money > 0:
    print(f"\n你当前余额为：{money} 元")
    
    # 获取下注金额
    while True:
        try:
            bet = int(input("请输入你要下注的金额（正整数）："))
            if 0 < bet <= money:
                break
            else:
                print("❌ 下注金额必须大于0，且不能超过当前余额！")
        except:
            print("❌ 请输入合法整数金额！")

    # 第一次摇骰子
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"🎲 第一次摇出：{die1} + {die2} = {total}")

    # 判断第一次结果
    if total in (7, 11):
        print("🎉 你赢了！")
        money += bet
    elif total in (2, 3, 12):
        print("💀 庄家胜，你输了。")
        money -= bet
    else:
        point = total
        print(f"🎯 游戏继续，你的点数是 {point}，继续摇骰子...")

        while True:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2
            print(f"🎲 又摇出：{die1} + {die2} = {total}")

            if total == point:
                print("🎉 你摇回了原来的点数，你赢了！")
                money += bet
                break
            elif total == 7:
                print("💀 摇到了 7，庄家胜！你输了。")
                money -= bet
                break
            else:
                print("🌀 游戏继续...")

print("\n💸 你已经破产，游戏结束！感谢游玩。")
