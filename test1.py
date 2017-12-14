# coding:utf-8

import urllib2
import cookielib
url ="http://www.baidu.com"

print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'
# 创建Request对象
request = urllib2.Request(url)

#添加http的header
request.add_header('User-Agent','Mozilla/5.0')
#发送请求获取数据
response2 = urllib2.urlopen(request)
print response2.getcode();
print len(response2.read())

print '第三中方法'
cj = cookielib.CookieJar()
opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
