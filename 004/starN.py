print('請輸入一個整數：', end = ' ')
n = input()
n = int(n)
i = 1
while i <= n:
    print('\n' + ' ' * (n - i) + '*' * (n - i + 1))
    i += 1
print('輸出結束！！！')
