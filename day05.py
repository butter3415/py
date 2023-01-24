# # dictionary (사전처럼)

# keys() - key 값만 추출
# fruits = {'apple' : '사과',
#           'watermelon' : '수박',
#           'strawberry' : '딸기',
#           'kiwi' : '키위',
#           'banana' : '바나나'}
#
# for k in fruits:    # keys 를 안쓰고 fruits 만 돌려도 default 값으로 key 값 출력
#     print(k)

# # keys()
# print(fruits.keys())    # key 값 추출
# # values()
# print(fruits.values())  # value 값 추출
# # items()
# print(fruits.items())   # key 와 value 동시 추출 # 튜플로 추출



# # 음식 추천 프로그램 만들기 v0.1 ~
#
# alcohol_foods = {'맥주' : '치킨',
#                  '와인' : '치즈',
#                  '고량주' : '마라탕',
#                  '소주' : '삼겹살'}
#
# alcohol = input('주문할 술(맥주/와인/고량주/소주)은? ')
# if  alcohol in alcohol_foods.keys():    # alcohol_food 키 중에 있으면 실행
#     print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))

# # 음식 추천 프로그램 만들기 v0.2 ~
#
# alcohol_foods = {'맥주' : '치킨',
#                  '와인' : '치즈',
#                  '고량주' : '마라탕',
#                  '소주' : '삼겹살'}
#
# while True:
#     alcohol = input('주문할 술(맥주/와인/고량주/소주/결제)은? ')
#     if alcohol == '결제':
#         print("안녕히 가십시오~")
#         break
#     if alcohol in alcohol_foods.keys():    # alcohol_food 키 중에 있으면 실행
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     else:
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))


# import random
#
# star = ['테란', '저그', '프로토스']
# print(random.choice(star))

# # 음식 추천 프로그램 만들기 v0.3 ~
#
# import random
#
# alcohol_foods = {'맥주' : '치킨',
#                  '와인' : '치즈',
#                  '고량주' : '마라탕',
#                  '소주' : '삼겹살'}
#
# while True:
#     alcohol = input('주문할 술(맥주/와인/고량주/소주/랜덤/결제)은? ')
#     if alcohol == '결제':
#         print("안녕히 가십시오~")
#         break
#     if alcohol in alcohol_foods.keys():    # alcohol_food 키 중에 있으면 실행
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     elif alcohol == '아무거나':
#         print(random.choice(list(alcohol_foods)))
#
#     else :
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))

alcohol_foods = {'맥주' : '치킨',
                 '와인' : '치즈',
                 '고량주' : '마라탕',
                 '소주' : '삼겹살'}

# copy()
# copy_alcohol = alcohol_foods
copy_alcohol = alcohol_foods.copy() # 별도 공간 할당해서 다른 메모리 주소 참조
copy_alcohol['소주'] = '두부김치'
print(copy_alcohol)
print(alcohol_foods)