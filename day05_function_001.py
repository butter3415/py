# # 함수의 매개변수로 함수 전달하기
# def print_hi(hi):
#     for k in range(5):
#         hi()
#
# def hi():
#     print('hello~')
#
# # hi()
# print_hi(hi)

# map(함수, 순환가능한 자료구조)
# 리스트, 딕셔너리, 문자열, 범위 range
def square(n):
    return n * n
def odd(n):
    return n % 2 == 1

# result = []
# for k in range(1, 6):
#     result.append(square(k))
# print(result)

print(list(map(square, [1,2,3,4,5])))
# map 함수는 list로 변경해야 사용 가능
# map 함수는 코드가 간결해짐

# 17-20 라인 4줄과 22라인 1줄의 실행 결과는 동일

# filter(함수, 순환가능한 자료구조)
print(list(filter(odd, [1,2,3,4,5])))

# 람다함수, 제너레이터