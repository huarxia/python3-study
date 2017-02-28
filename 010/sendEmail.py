#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib;
from email.mime.text import MIMEText

def send_email(host, username, psd, send_to, subject, content):
    msg = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
    msg['From'] = username
    msg['Subject'] = u'%s' % subject
    msg['To'] = ",".join(send_to)

    try:
        s = smtplib.SMTP_SSL(host, 465)
        s.login(username, psd)
        s.sendmail(username, send_to, msg.as_string())
        s.close()
    except Exception as e:
        print('Exception: send email failed', e)

if __name__ == '__main__':
    host = 'smtp.mxhichina.com'
    username = 'liubiao@itoxs.com'
    passwd = raw_input('请输入您的密码: ')
    to_list = ['huaxia@itoxs.com']
    subject = "邮件主题"
    content = '您好~~ 我的朋友,我正在使用Python爬蟲发送邮件~~'
    send_email(host, username, passwd, to_list, subject, content)
