#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-15 17:50:36
# @Author  : 花夏 (bliu@huikedu.com)
# @Link    : https://github.com/huarxia
# @Version : $Id$

import sys
import urllib2
import re
import pickle
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    """获取链接列表主方法
    """
    url = 'http://bb.0791gs.cn/vod-play-id-9901-src-1-num-25.html'
    content = urllib2.urlopen(url).read().encode('utf-8') 
    res_tr = r'<ul class="playul">(.*?)</ul>'
    # 得到的结果是一个数组
    # 类似： ['<li class=""><a target="_self" href="/vod-play-id-9901-src-1-num-25.html" title="第55集">第55集</a></li>']
    result =  re.findall(res_tr, content, re.S|re.M)
    print(result)
    # print(len(foundA)) 实际测试获取的是当前页所有的正确链接

    hrefArray = []
    fileData = readFile('./episode.json').split(',')
    for item in result:
        # print(item)
        linkPattern = re.compile("href=\"(.+?)\"")
        href = linkPattern.findall(item)
    # print(hrefArray)
    saveHrefJson('./episode.json', hrefArray)
    hrefSendedFileData = readFile('./hrefs.json').split('\n\n')
    hrefSendedFileData.pop(len(hrefSendedFileData) - 1)
    hrefSendedStr = '\n\n'.join(hrefSendedFileData) + '\n\n'

def saveHrefJson (fileName, hrefArray):
    """将获取到的链接列表存到本地，每次发送邮件，检查一遍师傅有重复，有则不发送邮件了~~
    """
    # print(hrefArray)
    output = open(fileName, 'w')
    output.write(str(hrefArray));
    output.close()
    # save(hrefArray)

def readFile (fileName):
    """读取文件并返回文件的内容
    """
    file_object = open(fileName)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close( )
    return all_the_text

def getreqHrefHtml (href):
    """根据链接列表里的href获取html并解析出邮件地址
    """
    content = urllib2.urlopen(href).read().decode('GBK').encode('utf8')
    res_tr = r'<td class="a-content">(.*?)</td>'
    result = re.findall(res_tr, content, re.S|re.M)
    email = re.findall(r"([_A-Za-z0-9-]+(?:\.[_A-Za-z0-9-\+]+)*)(@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*(?:\.[A-Za-z]{2,})) ?", result[0])
    if len(email) > 0 and email[0] and len(email[0]) >= 2:
        email = email[0][0] + email[0][1]
    return email

def getEmailOfHreflist (hrefArray):
    emailList = []
    for item in hrefArray:
        item = 'http://www.newsmth.net' + item
        email = getreqHrefHtml(item)
        if email:
            emailList.append(email)
    # print(emailList)
    # 将新的email添加到本地文件中
    fileData = readFile('./data/email.json').split(',')
    emailListData = []
    for item in emailList:
        if fileData:
            for listData in fileData:
                state = 0
                if item == listData:
                    state += 1
        if state <= 0:
            emailListData.append(str(item))
    saveHrefJson('./data/email.json', emailListData)
    return emailListData

###############################################################################
if __name__ == "__main__":
    main()
