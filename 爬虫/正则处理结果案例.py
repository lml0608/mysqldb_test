# -*- coding:utf-8 -*-  
'''
__author__:liubin 

 http: //www.neihan8.com/article/list_5_1 .html

'''


import urllib2

import re
#<div.*?class="f18 mb20">(.*?)</div>

class Spider:

    '''
    '''

    def loadPage(self,page):
        #请求的url
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0"

        header = {'User-Agent': user_agent}

        req = urllib2.Request(url,headers=header)

        response = urllib2.urlopen(req)

        html = response.read()
        gbk_html = html.decode('gbk').encode('utf-8')

        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)

        #print pattern

        item_list = pattern.findall(gbk_html)

        for i in item_list:
            print i


        #print item_list


        #return html


if __name__=='__main__':

    # print '请按下回车开始'
    # raw_input("page:")

    mySpider = Spider()
    mySpider.loadPage(1)



