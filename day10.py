from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="http://www.inha.ac.kr">인하대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""

# 인하대학교의 url 주소는 http://www.inha.ac.kr입니다.

soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a")  # return list 리스트

# print(urls)
for url in urls:
    print('{0}의 url주소는 {1}입니다.'.format(url.string, url.attrs['href']))


# university = soup.find(id='univ')
# contents = soup.find(id='contents')
#
# print(university.string)
# print(contents.string)

