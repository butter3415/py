import urllib.request
from bs4 import BeautifulSoup

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=105'
urls = urllib.request.urlopen(api).read()
soup = BeautifulSoup(urls, 'html.parser')
cities = soup.find_all("city")  # return list 리스트
datas = soup.find_all("data")
# wfs.pop(0)  # 맨 앞의 wf 태그 내용은 중기 날씨 요약 뉴스

# print(urls)
for i in range(len(cities)):
    print(f'{cities[i].string}의 날씨는 {datas[i*13].wf.string} 입니다.')



# import urllib.request
# from bs4 import BeautifulSoup
#
# api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=105'
# urls = urllib.request.urlopen(api).read()
# soup = BeautifulSoup(urls, 'html.parser')
# cities = soup.find_all("city")  # return list 리스트
# wfs = soup.find_all("wf")
# wfs.pop(0)  # 맨 앞의 wf 태그 내용은 중기 날씨 요약 뉴스
#
# # print(urls)
# for i in range(len(cities)):
#     print(f'{cities[i].string}의 날씨는 {wfs[i*13].string} 입니다.')


