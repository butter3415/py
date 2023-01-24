# module preview
# 파이썬 코드 파일 - 모듈
# 모듈 이용하여 파일 분리, 공유

# built in module 내장(표준)모듈
from math import *
import random as rd

print(ceil(3.1))   # 올림 함수(ceil)
print(floor(4.9))
print(sqrt(16))     # square root - sqrt 제곱근
print(rd.randint(1, 6))

# 사용자 정의 모듈
# import day05_myMath # (1)
#   길게 써야함 파일명을 다 써야 함수 호출 가능
# from day05_myMath import * # (2)
#   충돌이 없을만한 상황에서 사용
#   from 모듈이름 import 가져오고 싶은 함수 또는 변수
#   모듈 이름을 생략하고 함수를 사용한다.

# import day05_myMath as m # (3)
#
# print(m.fibo_recursion(6))
# print(m.power(2,10))

# print(day05_myMath.factorial_loop(5))
# print(day05_myMath.square(5))
# print(day05_myMath.power(2, 10))

