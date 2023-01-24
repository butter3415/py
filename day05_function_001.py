# 함수 (Function)
# 한가지 작업을 수행하도록 디자인된 코드블럭 or 코드의 집합

# 함수 선언 def
# def test(name):
#     print("hi! " + name)
#     return '이름을 출력함'
#     # return 에 아무것도 작성하지 않으면 None 출력
#
#
# test('python')  # Function call
# print(test('C++'))

# def minus(a, b):
#     """
#     두 수의 차를 구하는 함수
#     매개변수는 a와 b로 받음
#     """  # 어떤 함수인지 잘 알 수 있도록 메모하는 기능(Document String)
#     return a - b
#
# print(minus(5)) # TypeError (매개변수를 총 2개 받아야하지만 1개를 받거나 3개를 받았을때 나오는 에러)
#
# # help(minus)
# # print(minus.__doc__)    # document String 나오게 하는 함수


# 가변 매개변수
# 가변 매개변수는 하나만 사용 * print_even(times, *values, *others) X
# 가변 매개변수 뒤에 일반 매개변수가 올 수 없음. * print_even(*values, times) X

# def print_even(times, *values): # for 문이 실행되는 횟수는 values의 갯수에 따라 다르다 => 이것이 가변 매개변수
#     for value in values:
#         print(times * value)
#
# print_even(2, -9, 11, 77, 6)   # -18, 22, 154 출력

# 기본 매개변수
# 기본 매개변수 뒤에 일반 매개변수가 올 수 없음. * print_default(times=3, value) X

def print_default(value, times = 3):
    print(times * value)

print_default(5) # 15 출력 ( 5 * 3 )
print_default(5, 2) # 10 출력 ( 5 * 2 ) => 매개변수를 별도로 입력하지 않으면 3을 사용하는 것이고, 입력하면 입력한 수로 함수 실행
