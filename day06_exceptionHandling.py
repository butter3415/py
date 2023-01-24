# exception handling

# try:
# 예외가 발생할 가능성이 있는 코드
# except:
# 예외가 발생했을 때 실행할 코드
# else:
# 예외가 발생하지 않았을 때 실행할 코드
# finally:
# 무조건 실행 / 예외가 발생 여부에 상관없이 실행하는 코드

try:
    c = list()
    c.append("사과")
    a = int(input())
    b = int(input())
    print(a / b)
    print(c[0])
except ZeroDivisionError:
    print("분모에 0이 올 수 없습니다.")
except ValueError:
    print("입력된 수는 정수가 아닙니다!")
except IndexError:
    print("리스트의 범위를 벗어난 인덱스가 사용되었습니다.")
except:
    print("무언가 에러가 발생했습니다.")
else:
    print("정상적으로 처리되었습니다.")
finally:
    print("예외 발생 여부에 상관없이 항상 실행됩니다.")


# a = input()
# b = input()

# print(a.isdigit(), b.isdigit())
#
# if a.isdigit() and b.isdigit(): # isdigit 는 숫자인지만 보기 때문에 -99 를 입력하면 False 가 나옴
#     print(int(a) + int(b))
# else:
#     print("입력된 수는 정수가 아닙니다.")

