def a():            # generator
    yield 1         # 함수가 멈추지 않고 계속 리턴함 / 일회용, 한번 순회하면 이후에 다시 순회 못함
    yield -9        # 최종 실행 이전에 값은 모두 지워진다.
    yield 3

def b():            # normal function
    return 1        # stop
    return -9   # 죽은 코드
    return 3    # die code

print(type(a()), b())     # <generator object a at 0x0000024F9B74B5E0> 1
c = a()
print(c)

for i in c:
    print(i)

for i in c:
    print(i)