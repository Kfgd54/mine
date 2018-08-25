import urllib
import urllib.request

httpHandler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(httpHandler)

#方式一：直接使用opener发起请求

#方式二：将opener作为参数，设置给urllib.request.urlopen
#opener变成全聚德联网请求
urllib.request.install_opener(opener)

#urllib.request.urlopen相当于使用opener.open()
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

