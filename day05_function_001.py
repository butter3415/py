# 함수 (Function cont.)
# 재귀함수 (자기 자신을 호출하는 함수)

# factorial(팩토리얼)
# 5! = 5 X 4 X 3 X 2 X 1 = 120

def factorial_recursion(n):
    """
    팩토리얼 by 재귀
    f(n) = n * f(n-1)
    f(3) = 3 * f(2)
         = 3 * 2 * f(1)
         = 3 * 2 * 1 * f(0)
         = 3 * 2 * 1 * 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)
def factorial_loop(n):
    """
    팩토리얼 by 반복문
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial_recursion(4))
print(factorial_recursion(6))
print(factorial_loop(4))
print(factorial_loop(6))

# fibonacci(피보나치)

def fibo_recursion(n):
    """
    f(n) = f(n-1) + f(n-2)
    f(1) = 1
    f(2) = 1
    f(3) = f(2) + f(1)
         = 1 + 1
    f(4) = f(3) * f(2)
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

for k in range(1,8):
    print('피보나치 {0} : {1}'.format(k, fibo_recursion(k)))

# 재귀함수는 성능 상의 문제가 있음 (숫자가 클수록 오버헤드가 많이 걸림)
#   -> 해결 방법 중 하나가 메모화


