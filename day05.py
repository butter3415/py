# tuple
# 순서를 가진다.
# immutable 불변, 상수의 리스트라고 할 수 있다.
# 튜플의 원소를 정의한 후에는 추가, 삭제, 수정 불가
# read only 읽기 전용
# packing, unpacking 존재 => packing, unpacking 원소의 개수가 같아야함.

# *** list = [] / dictionary = {} / tuple = ()

# empty = ()
# numbers = (1, -9, 7)
# print(type(empty))
# print(numbers)
# print(numbers[-1])
# # numbers[0] = 5  # 원소 수정 안됨.

# subjects = ('python', 'c++', 'english', 'math') # packing
# for subject in subjects:
#     print(subject)
#
# NamCS, KimTG, Conner, ChoiSY = subjects # unpacking
# print(KimTG, NamCS, Conner)

a = input()
b = input()
# t = b
# b = a
# a = t
a, b = (b, a) # packing 과 unpacking 을 동시에 수행
print(a, b)