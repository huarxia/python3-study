# 利用 `for` 循环打印上边 列表中的每个内容
# ['花夏', 88, '魚陽', 90, 'liubiao', 85, '2333', 90, '秋舞斜阳', 88]

member = ['花夏', 88, '魚陽', 90, 'liubiao', 85, '2333', 90, '秋舞斜阳', 88]

index = 0
length = len(member)

while index < length:
    print(member[index], member[index+1])
    index += 2
