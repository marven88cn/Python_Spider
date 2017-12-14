# Python_Spider
python实现简单的爬虫数据demo
#### test1.py和test2.py是以下文章的源码。有需要直接下载，不喜勿喷
https://github.com/marven88cn/Python
#### baike目录的demo是简单实现爬取百度百科python词条内容
### 实例爬虫步骤：
 确定目标 （百度百科python）--- 分析目标（url 格式，数据格式，网页编码） -- 编写代码 -- 执行爬虫
### 目标：百度百科Python词条相关网页 标题 简介  url
#### 入口页 https://baike.baidu.com/item/Python/407313.htm
#### URL格式
 标题 ：
 ```python
 <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
 ```
 简介：
 ```python
 <div class="lemma-summary">
 ```
#### 页面编码 
```python
UTF-8
```
### 编写代码
```python
if __name__ == '__main__':
    # 设置入口url
    root_url = 'https://baike.baidu.com/item/Python/407313.htm'
    # 初始化
    obj_spider = SpiderMain()
    # 启动
    obj_spider.craw(root_url)

```
详细代码 看源码
 
 
