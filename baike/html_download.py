# coding:utf-8
import urllib2

# html下载器
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
