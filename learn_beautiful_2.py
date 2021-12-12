from bs4 import BeautifulSoup
import re
html_doc = """
<html>
    <head>
    <title>Simple test</title>
    </head>
    <body>
    <p id="China">中国，<b>你好!</b>。 </p>
    <p id="World">世界，<b>大同!</b>。 </p>
    </body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.head)
body = soup.body
china = soup.find_all('p',{'id':"China"})
key = soup.body
xx = u"([\u4e00-\u9fff])"#用re库来识别中文字符
chinese = re.compile(xx)
results = chinese.findall(html_doc)
for result in results:
    print(result,end='')
