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
import crawling

#! 发送邮件函数
def send_email(host, username, psd, send_to, bcc, subject, content):

    """发送邮件函数
    """
    msg = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
    msg['From'] = username
    msg['Subject'] = u'%s' % subject
    msg['To'] = ",".join(send_to)
    # msg['Bcc'] = ",".join(bcc)
    try:
        s = smtplib.SMTP_SSL(host, 465)
        # s.login(username, psd)
        # s.sendmail(username, send_to, msg.as_string())
        # s.close()
        fileData = crawling.readFile('./data/sended.json').split('\n\n')
        fileData.pop(len(fileData) - 1)
        emailStr = '\n\n'.join(fileData) + '\n\n'
        print('发送对象: ')
        for e in msg['To'].split(','):
            print(e)
            state = 0
            for item in fileData:
                if e == item:
                    state += 1
            if state <= 0:
                e += '\n\n'
                emailStr += e
        print('邮件发送成功...')
        print('发送地址见本地【data】文件夹\n')
        print('--------------------------------------------')
        crawling.saveHrefJson('./data/sended.json', emailStr)
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
        elif ch == b'\x1b': # esc 退出程序
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

    print('正在发送邮件...\n')
    # to_list = ['liubiao0810@live.cn', '769904012@qq.com']
    # 抄送人
    bcc = ['769904012@qq.com']
    # 调用另一个文件,一斤写好可以爬取水木社区的招聘信息
    to_list = crawling.main()
    # print(to_list)
    subject = '应聘高级前端工程师_刘彪'
    with open('./templet.html', 'rt') as f:
        data = f.read()
    content = data
    # 针对求职邮件应该单独发送
    for email in to_list:
        emailList = []
        emailList.append(email)
        # emailList.append('huaxia@itoxs.com')
        send_email(host, username, passwd, emailList, bcc, subject, content)
