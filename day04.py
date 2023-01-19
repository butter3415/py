import copy

odds = list(range(1, 11, 2))
print(odds)

# mixed = [3, 4, 1, 7, 'A', '한', '김', 5, 'b', 'B']    # 수치형은 int/ 문자는 str => 비교가 안됨
# TypeError: '<' not supported between instances of 'str' and 'int'

mixed = ['3', '4', '1', '7', 'A', '한', '김', '5', 'b', 'B']
# ascending : arabic number, alphabet UpperCase, alphabet LowerCase, Korean
# 오름차순 : 숫자, 대문자, 소문자, 한글
mixed.sort(reverse=True) # descending
# print(mixed)

# copy 방법
# a = [1,2,3]
# b = a.copy() # copy 함수 써서 복제
# c = list(a)  # 리스트 이용해서 복제본 만들었음
# d = a[:]    # 1 에서 끝까지 복제
#
# a[1] = 'inha'
# c[2] = 'univ'
#
# print(a, b, c, d)

# a = [1, [9, -7], 3]
# b = a.copy() # copy 함수 써서 복제
# c = list(a)  # 리스트 이용해서 복제본 만들었음
# d = a[:]    # 1 에서 끝까지 복제
#
# # a[1] = 'inha'
# a[1][0] = -99   # 다른 복제본에도 영향을 줌. b, c, d [1][0]번 방에도 -99로 변경
#
# print(a, b, c, d)

a = [1, [9, -7], 3]
b = copy.deepcopy(a)

a[1][1] = 'inha'
print(a, b)
