# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import urllib2

response = urllib2.urlopen("http://www.baidu.com")

html = response.read()

print html