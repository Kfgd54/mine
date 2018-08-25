import urllib
import urllib.request

import urllib.parse

#进行网络请求的时候，url不能包含中文
#讲中文转换成url编码
key = input('请输入查询的关键字：')

url = 'https://www.baidu.com/s?ie=UTF-8&wd=%s/'


#将字符串进行转码
key = urllib.parse.quote(key)

print(key)
url = url%(key)
print(url)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)