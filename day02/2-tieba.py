import urllib
import urllib.request
import urllib.parse

url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}

def write_to_file(content, i):
    with open('./download/贴吧第%d页.html' % (i + 1), mode='wb')as fp:
        fp.write(content.encode('utf-8'))
    print('贴吧第%d页保存成功' % (i + 1))


def load_url_data(key, num):
    for i in range(num):
        url_detail = url % (key, i * 50)

        request = urllib.request.Request(url=url_detail, headers=headers)

        response = urllib.request.urlopen(request)

        # read方法只能读一次
        content = response.read().decode('utf-8')

        write_to_file(content,i)

key = input('请输入贴吧：')

# urllib.parse.unquote()
key = urllib.parse.quote(key)

try:
    num = int(input('请输入爬取多少页：'))
except Exception as e:
    print('请输入数字：')
    num = int(input('请输入爬取多少页：'))

# alt+回车
load_url_data(key, num)
