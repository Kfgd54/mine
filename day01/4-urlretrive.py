import urllib
import urllib.request

url = 'http://vs6.bdstatic.com/browse_static/v3/common/widget/global/player/newPlayer_e2332cd1.swf'

urllib.request.urlretrieve(url=url, filename='./movie.swf')