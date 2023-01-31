from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1>인하대학교</h1>
<h2>소프트웨어융합공학과</h2>
<p>웹 스크레이핑</p>
<p>파이썬 기본 문법, 판다스, 스크레이핑, GUI ... </p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
t = soup.html.head.title
h1 = soup.html.body.h1.string
p1 = soup.html.body.p   # p 태그 두개면 위에 있는 p 태그 내용 나옴
p2 = p1.next_sibling.next_sibling

print(p1.string)
print(p2.string)
print(h1)
print(t)
print(t.string)