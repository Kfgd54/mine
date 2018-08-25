import urllib
import urllib.request

url = 'https://www.douban.com/people/139553691/'

#Cookie 模拟登陆
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
'Referer':'http://fanyi.baidu.com/',
'Cookie':'ll="118237"; bid=Mdy6-Gs5ktg; _vwo_uuid_v2=D2605DE195772B48CCA82B8773A7AABCC|614d0d0b8161d9e732e56fe801551b2a; douban-fav-remind=1; __yadk_uid=3ea1BPro7wI3p7RtuUJw5iUKINLJ3LBa; ap=1; ps=y; dbcl2="139553691:8ofB4xOVloM"; ap_6_0_1=1; push_noty_num=0; push_doumail_num=0; ct=y; gr_user_id=291f0d87-78bd-44ec-9eee-93e6784cb039; ck=DrvC; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1535033923%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DzZkTi8uc2h_bhIfK5oQZXvDX2oqviXGHvYCuqFAppw6z_heN3x45OX_9yMH-l8ay%26wd%3D%26eqid%3Dd1b738b300109a31000000035b7ec23f%22%5D; _pk_ses.100001.8cb4=*; ap_v=1,6.0; _pk_id.100001.8cb4=ff58340b306caa4d.1532339558.9.1535034024.1534982632.'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))