# coding:utf-8

# 入口函数
from baike import url_manger, html_download, html_parse, html_outprint


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manger.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parse.HtmlParser()
        self.outprint = html_outprint.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont= self.downloader.download(new_url)
                new_urls ,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outprint.collect_data(new_data)

                if count == 100:
                    break
                count  = count+1
            except:
              print 'craw failed'
        self.outprint.output_html()


if __name__ == '__main__':
    # 设置入口url
    root_url = 'https://baike.baidu.com/item/Python/407313.htm'
    # 初始化
    obj_spider = SpiderMain()
    # 启动
    obj_spider.craw(root_url)







