# 내일은 새로운 gmail 계정 준비하쟈 -> git, github 수업 위하여
# 오픈소스로 사용할 수 있도록 하겠어요 둑흔

import copy
a = ['김지혜', '곽다인', '김설화', '이영철', '조희령']

b = copy.deepcopy(a) # 다른 메모리 주소를 참조한다.
print(b, a)

a[0] = '김인하'

print(b, a)

print (id(a), id(b)) # a 와 b는 참조 변수일 뿐 메모리 공간은 2라인의 저 공간 밖에 없음

# b = a 하면
# 사물함 같이 쓰고 있음 (a, b)

# x = 99
# y = x + 5
# print(y)

# b = a -> 같은 객체 가리킴
# 31 페이지 타입 키워드로 어떤 자료형 객체를 박싱하고 있는지 확인 가능

# literal
# 77 = 99
# 'univ' = 'inha'

# #type
# print(type(2.7e-1))
#
# countdown_tuple = (5,4,3,2,1, "hey!")
# # countdown_tuple[2] = -99    #TypeError: 'tuple' object does not support item assignment -> 원소 값 못 바꿉니다
# # tuple is immutable
# temp = list(countdown_tuple)
# temp[2] = -99 # mutable
# countdown_tuple = tuple(temp)
# print(countdown_tuple[2]) # 3 -> -99
#
# for countdown in countdown_tuple:
#     print(countdown)
#
# countdown_list = [5,4,3,2,1,"hey!"]
# countdown_list[2] = -99     # mutable 변경 가능
#
# for countdown in countdown_list:
#     print(countdown)

# 화씨 섭씨 온도 변환 프로그램
# (100°F − 32) × 5/9 = 37.778°C

# fahrenheit = float(input("화씨온도 : "))
# celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
# print('화씨 온도 ', fahrenheit,'도는 섭씨온도 ',celsius,'도 입니다.')     # comma 콤마
# print('화씨 온도 %.2f도는 섭씨 온도 %.2f도 입니다' %(fahrenheit, celsius))    # old style
# print('화씨 온도 {0:.2f}도는 섭씨 온도 {1:.2f}도 입니다' .format(fahrenheit, celsius))    # modern style
# # 이 경우는 순서를 바꿔서 입력할 수도 있음. {1:.2f} / {0:.2f} 와 같이 하면 celsius 먼저 나옴.
# print(f'화씨 온도 {fahrenheit:.2f}도는 섭씨 온도 {celsius:.2f}도 입니다')    # newest style, f-style

# 객체는 포장되어 있는 박스에 들어있다.
# 인트라는 박스에 7이라는 객체가 들어가있다.