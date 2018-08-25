import urllib
import urllib.request

#HttpHandler 类似

proxies = {'http':'113.99.218.244:53281'}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(fullurl='http://www.baidu.com')

print(response.read().decode('utf-8'))