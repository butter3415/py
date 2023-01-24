# exception handling (cont.)

def midterm():
    score = int(input('1에서 10 사이의 정수 입력 : '))
    if score < 0 or score > 10 :
        raise Exception("중간고사 점수 입력 범위를 벗어났습니다. {0}점 입력 불가".format(score))
    else:
        print('{0}점 입니다.'.format(score))

try:
    midterm()
except Exception as e:
    print("예외 발생 : {0}".format(e))

# try:
#     print(5/2)
#     b = int(input())
#     a = [1, 2, 3]
#     print(a[1])
#     raise Exception("지혜가 만든 예외")    # raise 일으키다 -> 예외를 일으키다
# except IndexError as e:
#     print("인덱스 범위를 벗어났습니다 : {0}".format(e))
# except ZeroDivisionError as e:
#     print("분모에 0이 올 수 없습니다 : {0}".format(e))
# except Exception as e:  # 맨 마지막에 작성 / 전체 조상 (다 잡아줌)
#     print("무언가 에러가 발생했습니다. : {0}".format(e))




