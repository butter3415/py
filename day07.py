import random

def calculate_fee(ages):   # list로 받는다
    total = 0
    adults = 0
    kids = 0

    for age in ages:
        if  19 <= age :    # adult
            total = total + 10000
            adults += 1
        else:   # kids
            total = total + 4000
            kids += 1
    return [len(ages), adults, kids, total]

# result = calculate_fee([7, 45, 43, 10])
no_of_visitor = int(input(f'몇 분이신가요~?! '))
ages = [random.randint(1, 100) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(ages)
print(f'{results[0]}명 방문 하셨고, 어른 {results[1]}명, 어린이 {results[2]}명, 총 요금은 {results[-1]}원입니다.')

# 출력 양식
# 3명 방문하셨고 어른 3명, 어린이 0명 총 요금은 30000원입니다.