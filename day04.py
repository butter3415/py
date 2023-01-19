import random

# hard coding
# numbers = list()
# numbers.append(random.randint(1, 100)) # 100 포함 랜덤수
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# print(numbers)

# for loop
# numbers = []
# for k in range(5):
#     numbers.append(random.randint(1,100))
# print(numbers)

# list comprehension
# numbers = [random.randint(1,100) for k in range(5)]
# print(numbers)

# odds = [k for k in range(1,11) if k % 2]
# for k in range(1, 11):
#     if k % 2 :
#         odds.append(k)
# print(odds)

odds = [k for k in range(1,11) if k % 2] # 변수 - for문 - if문 /// k % 2 == 1 -> True
print(odds)

# join 은 문자열에서 사용 가능하기 때문에 정수타입 리스트를 문자열로 변경해서 출력

# 해결방법 1. index
# for i in range(len(odds)):
#     odds[i] = str(odds[i])
# print(odds)
# print(' / '.join(odds)) # 리스트의 원소들을 하나의 문자열로 만들어준다.

# 해결방법 2. list
# temp = list()
# for odd in odds:
#     temp.append(str(odd))
# print(temp)
# print(' / '.join(temp))

# 해결방법 3. enumerate
for item in enumerate(odds):    # (index, value) 튜플 형태로 리턴
    # print(item) # 튜플 형태로 출력 (0,1) (1,3) (2,5) ...
    odds[item[0]] = str(item[1])
print(odds)
print(' / '.join(odds))