# 음식 추천 프로그램 만들기 v0.7 ~

import random

alcohol_foods = {}
a = input('술의 종류를 보관하고 있는 파일은? ')
f = input('안주의 종류를 보관하고 있는 파일은? ')

try:
    with open(a) as fp1:
        with open(f) as fp2:
            alcohols = fp1.readlines()  # 리스트 변수 alcohols
            foods = fp2.readlines() # 리스트 변수 foods
            for k in range(len(alcohols)):
                alcohol_foods[alcohols[k].strip('\n')] = foods[k][0:-1]   # strip('\n') -> \n 떨궈내기 위함
except FileNotFoundError as e:
    print("파일이 없거나 폴더 경로가 틀렸습니다 :", e)
else:
    while True:
        alcohol = input('주문할 술('+ '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) + '/아무거나/결제)은? ')
        if alcohol == '결제':
            print("안녕히 가십시오~")
            break
        if alcohol in alcohol_foods.keys():    # alcohol_food 키 중에 있으면 실행
            print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
        elif alcohol == '아무거나':
            any = random.choice(list(alcohol_foods))
            print('{0}을(를) 추천합니다. 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
        else :
            print('{0}은(는) 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))
finally:
    print("다음에 또 만나요~!")