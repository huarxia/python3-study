# 使用if判斷將成績分數轉換為 A B C D四個檔次
# 90~100: A
# 80~89: B
# 60~79: C
# 0~59: D
# 且 平均成绩一般集中在 70~80 分之间，要求提高程序效率

score = input('請輸入成績: ')
grade = 'A'
while not score.isdigit():
    score = input('您輸入的不是一個數字,請重新輸入: ')
score = int(score)

while score < 0 or score > 100:
    score = input('您輸入的不是成績是什麼鬼,請輸入一個0~100的成績數: ')
    # 每次輸入后需要將其轉換為數字，否則hi報錯
    score = int(score)

if 60 <= score < 80:
    grade = 'C'
elif 80 <= score < 90:
    grade = 'B'
elif 90 <= score <= 100:
    grade = 'A'
else:
    grade = 'D'

print('您的成績等級是: ', grade)
