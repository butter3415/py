# def a():    # decorator 꾸며준다. 그냥 꾸며주는 역할, closer 사용한다
#     def b():
#         return "안쪽 함수 실행"
#     return b()
#
# print(a())
# print(b())  # a 함수에서만 볼 수 있다.

def a():    # decorator 꾸며준다. 그냥 꾸며주는 역할, closer 사용한다
    def b():
        return "안쪽 함수 실행"
    return b

print(a())
c = a()
print(c())

# 스코프 -> 볼 수 있는 영역, 범위