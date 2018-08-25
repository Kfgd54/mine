import urllib
import urllib.request

url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')

print(content)