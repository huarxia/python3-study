#!/usr/bin/python
#-*-coding:utf-8-*-


def pwd_input():
    import termios
    """输入密码替换为星号
    :return: 字符串形式密码
    """
    chars = []
    while True:
        try:
            new_char = termios.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        if new_char in '\r\n':  # 如果是换行，则输入结束
            break
        elif new_char == '\b':  # 如果是退格，则删除密码末尾一位并且删除一个星号
            if chars:
                del chars[-1]
                termios.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
                termios.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
                termios.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
        else:
            chars.append(new_char)
            termios.putch('*'.encode(encoding='utf-8'))  # 显示为星号
    print('')
    return ''.join(chars)

print('按回车键退出')
