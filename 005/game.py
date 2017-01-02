import random
times = 3
secret = random.randint(1, 10)
print('------------------我爱python------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，觉得富有创意的你应该会尝试用 end="🐍"？
# print("不妨猜一下我現在现在心里想的是哪个数字🐍 : ", end = " ")
while (guess != secret) and (times > 0):
    temp = input("不妨猜一下我現在现在心里想的是哪个数字🐍 : ")
    # 這裡不能使用if; 試想下，用if再次輸入事是不是還需要繼續判斷呢？
    while not temp.isdigit():
    	temp = input('不好意思，您輸入的不是一個整數，請重新輸入: ')
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是我心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")
