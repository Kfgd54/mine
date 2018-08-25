import urllib
import urllib.request
import urllib.parse
import json

#post请求
url = 'http://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
'Referer':'http://fanyi.baidu.com/',
'Cookie':'BAIDUID=55754BD6F0D84A34D3C9DE439F0B4D81:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=55754BD6F0D84A34D3C9DE439F0B4D81; PSTM=1532316457; BDUSS=l3bHdHek4xVE5jdnVqbEc4c2Z2NkdlUn56MEhhWDdvNkRmRVM4aXNqVW9BSDViQVFBQUFBJCQAAAAAAAAAAAEAAACeVg9kUG3X07quAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChzVlsoc1ZbQm; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1534508932,1534769813,1534946277,1535024583; H_PS_PSSID=1437_21126_26920; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1535027545; from_lang_often=%5B%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
'Host':'fanyi.baidu.com'}

'''from=zh&
to=en&
query=%E4%B8%AD%E5%9B%BD&
transtype=enter&
simple_means_flag=3&
sign=777849.998728&
token=4d4053b5aa51c9c901cfe93d5ff1e320'''

key = input('请输入翻译的汉字：')

form = {'from':'zh',
        'to':'en',
        'query':key,
        'trtranstype':'enter',
        'simple_means_flag':3,
        'sign':'777849.998728',
        'token':'4d4053b5aa51c9c901cfe93d5ff1e320'}

form = urllib.parse.urlencode(form).encode('utf-8')

request = urllib.request.Request(url=url, headers=headers, data=form)

#直接使用urlopen没有获取
# response = urllib.request.urlopen(url=url, data=form)

#request  构建请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = json.dumps(json.loads(content, encoding='utf-8'), ensure_ascii=False)

print(content)