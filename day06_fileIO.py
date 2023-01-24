# file io
# Open, Close 파일 있음.

# 파일 객체명 = open(파일 경로, 읽기 모드) * 파일 경로, 읽기 모드 - 문자열
# w : 쓰기 모드(write), r : 읽기모드(read), a : 이어쓰기 모드(append)
# 파일을 닫을 때 : 파일객체명.close()

# 파일 쓰기
# fp = open('war_flower.txt', 'w')
# print('고니', file=fp) # 실제 쓰기
# print('정마담', file=fp) # 실제 쓰기
# print('아귀', file=fp) # 실제 쓰기
# fp.write('너부리') # 실제 쓰기
# fp.close() # 열었으니까 닫기

# 파일 읽기 (default 모드가 r (읽기 모드))
# fp = open('war_flower.txt', 'r')
# lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
# # print(lines)
#
# for line in lines:
#     # print(line.rstrip('\n'))
#     # print(line[:-1])
#     # print(line, end='')
#
# fp.close()

# with
with open('war_flower.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        print(line[:-1])
