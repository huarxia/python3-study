#coding=utf-8
# Python 爬取水木社區招聘網站招聘信息

import sys
import urllib2
import re
import pickle
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    """获取链接列表主方法
    """
    url = 'http://www.newsmth.net/nForum/s/article?ajax&t1=%25E5%2589%258D%25E7%25AB%25AF&au=&b=Career_Upgrade'
    content = urllib2.urlopen(url).read().decode('gbk').encode('utf8')
    # print(content)
    # you should see the ouput html
    # <td class="title_14">
    #     <a target="_blank" href="/nForum/article/Career_Upgrade/500193" title="在新窗口打开此主题">
    #         <samp class="tag ico-pos-article-normal"></samp>
    #     </a>
    # </td>
    res_tr = r'<td class="title_14">(.*?)</td>'
    # 得到的结果是一个数组
    # 类似： ['<a target="_blank"href="/nForum/article/Career_Upgrade/500269" title="aaa"><samp class="tag ico-pos-article-normal"></samp></a>']
    result =  re.findall(res_tr, content, re.S|re.M)
    # print(len(foundA)) 实际测试获取的是当前页所有的正确链接
    # print(result)

    hrefArray = []
    fileData = readFile('./data/hrefArray.json').split(',')
    for item in result:
        # print(item)
        linkPattern = re.compile("href=\"(.+?)\"")
        href = linkPattern.findall(item)
        # print(href)
        if fileData:
            for listData in fileData:
                state = 0
                if href[0] == listData:
                    state += 1
        if state <= 0:
            hrefArray.append(str(href[0]))
    # print(hrefArray)
    saveHrefJson('./data/hrefArray.json', hrefArray)
    return getEmailOfHreflist(hrefArray)

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
    # getreqHrefHtml('http://www.newsmth.net//nForum/article/Career_Upgrade/499906')
    emailList = main()
    print(emailList)
