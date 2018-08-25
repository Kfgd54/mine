import urllib
import urllib.request

url = 'https://www.baidu.com/'

#构造请求头
########爬虫时的第一层伪装##############
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)