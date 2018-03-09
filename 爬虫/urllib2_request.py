# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import urllib2

url = "http://www.baidu.com"

ua_header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0"}

# url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib2.Request(url,headers = ua_header)

request.add_header("Connection","keep-alive")

print request.get_header("User-agent")



response = urllib2.urlopen(request)

print response.code  #200

html = response.read()

print html