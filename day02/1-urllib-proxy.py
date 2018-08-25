import re
import urllib
import urllib.request

'''
<tr class="odd">
    <td class="country"><img src="./免费代理IP_HTTP代理服务器IP_隐藏IP_QQ代理_国内外代理_西刺免费代理IP_files/cn.png" alt="Cn"></td>
    <td>119.10.67.144</td>
    <td>808</td>
    <td>北京</td>
    <td class="country">高匿</td>
    <td>HTTPS</td>
      <td>18天</td>
    <td>1分钟前</td>
  </tr>
'''

pattern = re.compile('<td>([\w\.]+)</td>')

with open('./proxy.html', mode='r', encoding='utf-8') as fp:
    proxy = fp.read()
    proxies = re.findall(pattern=pattern, string=proxy)

    print(proxies)
    print(len(proxies))