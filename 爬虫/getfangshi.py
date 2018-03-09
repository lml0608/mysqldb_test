# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import urllib      #负责url编码处理
import urllib2


def loadPage(fullurl, filename):

    print "正在下载" +filename

    ua_header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0"}

    request = urllib2.Request(url, headers=ua_header)
    response = urllib2.urlopen(request)

    return response.read()

def tiebaSpider(url,beiginPage,endPage):


    for page in range(beiginPage,endPage+1):

        pn = (page - 1) * 50

        filename = "the" + str(page) + "page.html"

        fullurl = url + "&pn=" + str(pn)

        html = loadPage(fullurl,filename)

        writeFile(html,filename)

def writeFile(html,filename):

    print "正在储存" + filename

    with open(filename,'w') as f:
        f.write(html)

    print "-" * 20

if __name__=="__main__":

    kw = raw_input("请输入需要爬取的贴吧：")

    beiginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入终止页:"))

    url = "http://tieba.baidu.com/f?"

    key = urllib.urlencode({"kw":kw})

    url = url + key

    tiebaSpider(url,beiginPage,endPage)







