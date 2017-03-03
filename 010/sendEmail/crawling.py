#coding=utf-8
# Python 爬取水木社區招聘網站招聘信息

import sys
import urllib2;
import re;
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    url = 'http://www.newsmth.net/nForum/s/article?ajax&t1=%25E5%2589%258D%25E7%25AB%25AF&au=&b=Career_Upgrade'
    content = urllib2.urlopen(url).read().decode('gbk').encode('utf8')
    print(content)
    # you should see the ouput html
    # <td class="title_14">
    #     <a target="_blank" href="/nForum/article/Career_Upgrade/500193" title="在新窗口打开此主题">
    #         <samp class="tag ico-pos-article-normal"></samp>
    #     </a>
    # </td>
    foundA = re.search('<td\s+?class="title_9">(?P<foundAHtml>.+?)</td>', content)
    print("foundA=", foundA)
    if(foundA):
        result = foundA.group("foundAHtml")
        print ('foundA=', foundA)

###############################################################################
if __name__ == "__main__":
    main()
