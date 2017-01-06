# 设计一个验证用户密码程序(密碼這裡使用huar.love);
# 用户只有三次机会输入错误;
# 不过如果用户输入的内容中包含"*"则不计算在内。

password = 'huar.love'
# 不能包含的特殊符號
specialCharacters = '*'

# 總共只有3次機會
count = 3
while count:
    psd = input('請輸入密碼: ')
    if password == psd:
        print('恭喜您,密碼校驗通過，請進入程序玩耍吧~~😄')
        break
    elif specialCharacters in psd:
        print('密碼中不能包含', specialCharacters, '您還有', count, '次機會~~(⊙o⊙)…')
    else:
        count -= 1
        print('密碼輸入錯誤！您還有', count, '次機會~~(⊙o⊙)…')
