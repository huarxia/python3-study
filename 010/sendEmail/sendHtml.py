#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib
import urllib2
from email.mime.text import MIMEText
import sys, tty, termios
import getpass

#! 发送邮件函数
def send_email(host, username, psd, send_to, subject, content):

    """发送邮件函数
    """
    msg = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
    msg['From'] = username
    msg['Subject'] = u'%s' % subject
    msg['To'] = ",".join(send_to)

    try:
        s = smtplib.SMTP_SSL(host, 465)
        s.login(username, psd)
        s.sendmail(username, send_to, msg.as_string())
        s.close()
        print('邮件发送成功...')
    except Exception as e:
        print('Exception: send email failed', e)

#！ 处理输入密码函数
def getch(): 
    
    """获取键盘输入函数
    """ 
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getpass(maskchar = "*"):

    """处理输入密码函数显示*函数
    """
    print('请输入电邮密码: ')
    password = ""
    while True:
        ch = getch()
        if ch == "\r" or ch == "\n" or ch == "\r\n":
            print
            return password
        elif ch == "\b" or ord(ch) == 127:
            if len(password) > 0:
                sys.stdout.write("\b \b")
                password = password[:-1]
        elif ch == b'\x1b':
            return None
            break
        else:
            if maskchar != None:
                sys.stdout.write(maskchar)
            password += ch

if __name__ == '__main__':
    host = 'smtp.mxhichina.com'
    username = 'liubiao@itoxs.com'
    passwd = getpass('*')
    while passwd == '':
        passwd = getpass("*")
    if passwd == None:
        print('输入结束,退出程序...')
        sys.exit()

    print('正在发送邮件...')
    to_list = ['769904012@qq.com']
    subject = '应聘高级前端工程师_刘彪'
    with open('./templet.html', 'rt') as f:
        data = f.read()
    content = data
    send_email(host, username, passwd, to_list, subject, content)
