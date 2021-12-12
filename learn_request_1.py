import requests
def GetHttp(Url):
    try:
        r = requests.get(Url,timeout = 30)
        r.raise_for_status() #若非200，则引发异常，使用此能代替多个if结构
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''
Url="http://www.baidu.com"
print(GetHttp(Url))
