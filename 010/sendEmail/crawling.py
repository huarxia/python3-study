#coding=utf-8
# Python 爬取水木社區招聘網站招聘信息

import sys
import urllib2;
import re;
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
    # print(len(foundA)), 实际测试获取的是当前页所有的正确链接
    # print(result)

    hrefArray = []
    for item in result:
        # print(item)
        linkPattern = re.compile("href=\"(.+?)\"")
        href = linkPattern.findall(item)
        # print(href)
        hrefArray.append(href[0])
    # print(len(hrefArray))
    # if(foundA):
    #     result = foundA.group("foundAHtml")
    #     print ('foundA=', foundA)

###############################################################################
if __name__ == "__main__":
    main()
