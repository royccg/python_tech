<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [理念](#理念)
- [Request 库](#request-库)
	- [入门](#入门)
	- [Response对象的属性](#response对象的属性)
	- [通用代码框架](#通用代码框架)
	- [理解Requests库的异常](#理解requests库的异常)
	- [Requests库的7个主要方法](#requests库的7个主要方法)
	- [HTTP协议对资源的操作](#http协议对资源的操作)
	- [request方法](#request方法)
	- [robots.txt 网络爬虫的盗亦有道](#robotstxt-网络爬虫的盗亦有道)
		- [网络爬虫的法律风险](#网络爬虫的法律风险)
		- [网络爬虫引发的问题](#网络爬虫引发的问题)
		- [网络爬虫的限制](#网络爬虫的限制)
		- [Robots协议的使用](#robots协议的使用)
	- [Requests库爬取实例](#requests库爬取实例)
		- [百度、360关键字提交](#百度360关键字提交)
		- [网络图片的爬取](#网络图片的爬取)
		- [ip地址归属地的自动查询](#ip地址归属地的自动查询)
- [Beautiful_Soup库](#beautifulsoup库)
	- [安装](#安装)
	- [使用](#使用)
	- [库的元素](#库的元素)
		- [理解](#理解)
		- [Beautiful Soup库解析器](#beautiful-soup库解析器)
		- [Beautiful Soup类的基本元素](#beautiful-soup类的基本元素)

<!-- /TOC -->

# 理念
Python网络爬虫与信息提取
```yaml
The Website is the API...
```
# Request 库
自动爬取HTML页面，自动网络请求提交
## 入门
```python
request.get(url, params=None, **kwargs)
```
+ `url`: 拟获取页面的**url**连接
+ `params`: **url**中的额外参数，字典或字节流格式，可选
+ `**kwargs`: 12个控制访问的参数

## Response对象的属性
+ `r.status_code`: HTTP请求的返回状态，`200`表示连接成功，`404`表示失败
+ `r.text`: HTTP响应内容的字符串形式，即，`url`对应的页面内容
+ `r.encoding`: 从HTTP header中猜测的响应内容编码方式
+ `r.apparent_encoding`: 从内容中分析出的响应内容编码方式（备选编码方式）
+ `r.content`: HTTP响应内容的二进制形式

注意：`r.encoding: 如果header中不存在charset，则认为编码为ISO_8859 - 1`

## 通用代码框架
## 理解Requests库的异常
异常 | 说明
:----| :----
`requests.ConnectionError`| 网络连接错误异常，如DNS查询失败、拒绝连接等
`requests.HTTPError`| HTTP错误异常
`requests.URLRequired`| URL缺失异常
`requests.TooManyRedirects`| 超过最大重定向次数，产生重定向异常
`requests.ConnectTimeout`| 连接远程服务器超时异常
`requests.Timeout`| 请求URL超时，产生超时异常

异常 | 说明
:----: |:----:
`r.raise_for_status()`| 如果不是`200`，产生异常`requests.HTTPError`

## Requests库的7个主要方法
异常 | 说明
:---- |:----
`requests.request()`| 构造一个请求，支撑以下各方法的基础方法
`requests.get()` | 获取HTML网页的主要方法，对应于HTTP的GET
`requests.head()`| 获取HTML防网页头信息的方法，对应于HTTP的HEAD
`requests.post()`| 向HTML网页提交POST请求的方法，对应于HTTP的POST
`requests.put()` | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT
`requests.patch()`| 向HTML网页提交局部修改请求，对应于HTTP的PATCH
`requests.delete()`| 向HTML网页提交删除请求，对应于HTTP的DELETE

## HTTP协议对资源的操作
|方法 | 说明|
|:-----:|:------:|
|`GET`| 请求获取URL位置的资源|
|`HEAD`| 请求获取URL位置资源的响应消息报告，即获得该资源的头部信息|
|`POST`| 请求向URL位置的资源后附加新的数据|
|`PUT`| 请求向URL位置储存一个资源，覆盖原URL位置的资源|
|`PATCH`| 请求局部更新URL位置的资源，即改变该处资源的部分内容|
|`DELETE`| 请求删除URL位置存储的资源|

## request方法
```python
requests.request(method, url, **kwargs)
method: 请求方法
r = requests.request('GET', url, **kwargs)
r = requests.request('HEAD', url, **kwargs)
r = requests.request('POST', url, **kwargs)
r = requests.request('PUT', url, **kwargs)
r = requests.request('PATCH', url, **kwargs)
r = requests.request('delete', url, **kwargs)
r = requests.request('OPTIONS', url, **kwargs)
```

```python
requests.request(method, url, **kwargs)
```
+ `**kwargs`:控制访问的参数，均为可选项
+ `params`: 字典或字节序列，作为参数增加到url中
+ `data`: 字典、字节序列或文件对象，作为Request的内容
+ `json`: JSON格式的数据，作为Request的内容
+ `headers`:字典，HTTP定制头
+ `cookies`: 字典或CookieJar, Request 中的Cookie
+ `auth`: 元组，支持HTTP认证功能
+ `files`: 字典类型，传输文件
+ `timeout`: 设定超时时间，秒为单位
+ `proxies`: 字典类型，设定访问代理服务器，可以增加登录认证
+ `allow_redirects`: True/False, 默认为True，重定向开关
+ `stream`: True/False，默认为True, 获取内容立即下载开关
+ `verify`: True/False，默认为True，认证SSL证书开关
+ `cert`: 本地SSL证书路径

## robots.txt 网络爬虫的盗亦有道
### 网络爬虫的法律风险
+ 服务器上的数据有产权归属
+ 网络爬虫获取数据后牟利将带来法律风险

### 网络爬虫引发的问题
+ 骚扰问题
+ 法律问题
+ 隐私泄露

### 网络爬虫的限制
+ 来源审查：判断`User-Agent`进行限制
    * 检查来访`HTTP`协议头的`User-Agent`域，只响应浏览器或友好爬虫的访问。
+ 发布公告： Robots协议
	+ 告知所有爬虫网站的爬取策略，要求爬虫遵守。

### Robots协议的使用
+ 网络爬虫给：自动或人工识别`robots.txt`，再进行内容爬取
+ 约束性：`Robots`协议是建议但非约束性，网络爬虫可以不遵守，但存在法律风险。

## Requests库爬取实例
### 百度、360关键字提交
1. 搜索引擎关键字提交接口
+ 百度的关键词接口：
	+ `http://www.baidu.com/s?wd=keyword`
+360的关键词接口：
	+ `http://www.so.com/s?q=keyword`

### 网络图片的爬取
+ 网络图片链接的格式：
	+ `http://www.example.com/picture.jpg`
+ 国家地理：
	+ `http://www.nationalgeographic.com.cn/`
+ 选择一个图片Web页面
	+ `http://www.nationalgeographic.com.cn/photography/photo_of_the_day/3921.html`

### ip地址归属地的自动查询
`http://m.ip138.com/ip.asp?ip=ipaddress`

# Beautiful_Soup库
## 安装
`pip install beautifulsoup4`

## 使用
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>', 'html.parser')
```

## 库的元素
### 理解
`Beautiful Soup`库是解析、遍历、维护“标签树” 功能库。

### Beautiful Soup库解析器
解析器 | 使用方法 |条件
:---|:---|:---
bs4的HTML解析器| `BeautifulSoup(mk,'html.parser')`|安装bs4库
lxml的HTML解析器|`BeautifulSoup(mk, 'lxml')`|`pip install lxml`
lxml的XML解析器|`BeautifulSoup(mk, 'xml')`|`pip install lxml`
html5lib的解析器|`BeautifulSoup(mk, 'html5lib')`|`pip install html5lib`

### Beautiful Soup类的基本元素
基本元素| 说明
:---|:---
`Tag`|标签，最基本的信息组织单元，分别用`<>`和`</>`标明开头和结尾
`Name`|标签和名i在，`<p>...</p>`的名字是`p`，格式：`<tag>.name`
`Attributes`|标签的属性，字典形式组织，格式：`<tag>.attrs`
`NavigableString`|标签内非属性字符串，`<>...</>`中字符串，格式：`<tag>.string`
`Comment`|标签内字符串的注释部分，一种特殊的`Comment`类型

## 基与bs4库的HTML内容遍历方法
### 标签树的下行遍历
属性|说明
`.contents`| 子节点的列表，将`<tag>`所有儿子节点存入列表
`.children`| 子节点的迭代类型，与`.contents`类似，用于循环遍历儿子节点
`.descendants`|子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

+ 遍历儿子节点
```python
for child in soup.body.children:
	print(child)
```
+ 遍历子孙节点
```python
for child in soup.body.descendants:
	print(descendants)
```

### 标签树的上行遍历
属性| 说明
`.parent`| 节点的父亲标签
`.parents`| 节点先辈标签的迭代类型，用于循环遍历先辈节点
