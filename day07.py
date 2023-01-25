# Closures 클로저
def calculate():
    x = 5
    y = 10
    def add_sub(n):     # inner function act as closure     # 바깥 애들 수를 기억함. x, y 값을 기억해서 계산해줌
        return x + n - y
    return add_sub      # 클로저 리턴

calc = calculate()
print(type(calc), calc)
print(calc(3))

for i in range(5):
    print(calc(i))