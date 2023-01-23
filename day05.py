# # dictionary (사전처럼)
#
# # 리스트와 비슷하나 순서를 따지지 않는다. (인덱스가 없다)
# # 키와 값이 pair가 원소가 된다.
# # { 'key' : 'value' }
#
#
# fruits = {'apple':'사과', 'watermelon':'수박'}
# print(fruits['watermelon']) # key 를 이용하여 해당 원소에 접근한다
#
# # 추가 / append 가 없음. append는 list 의 함수
# print(fruits)
# fruits['kiwi'] = '키우이'   # 삽입
# print(fruits)
#
# fruits['kiwi'] = '키위'   # 수정
# print(fruits)
#
# fruits['banana'] = '바나나' # 삽입
# # ★ key 값은 중복이 안된다. 유일해야한다!!!
#
# empty = {}
# print(type(fruits), type(empty))    # 둘 다 dictionary

# #dict 함수
# test1 = [['python','3'],['english','2'],['dance','1']]     # test의 원소는 3개 (0번, 1번, 2번 방)
# print(test1[1][0])
# print(dict(test1))   # dictionary 로 변환
#
# test2 = ['ab', 'cd', 'ef']      # 문자열 구분해서 dictionary로 만들어줌
# print(test2[1][0])
# print(dict(test2))
#
# # ★ key : value 형식이기 때문에 2개의 원소가 필요하다!!! - 짝을 맞춰줘야함.

# update() 결합
fruits = {'apple' : '사과', 'watermelon' : '수박', 'banana' : '버내너~'}
# print(fruits)

others = {'strawberry' : '딸기', 'kiwi' : '키위', 'banana' : '바나나'}
# ★ 중복 키 있을 경우 합쳐지는 key 값의 내용으로 업데이트
fruits.update(others) # 해당 dirctionary명.update()
print(fruits)

# del - 삭제
del(fruits['apple'])
print(fruits)

# clear - dictionary 안 모든 원소 전체 삭제
fruits.clear()
print(fruits)