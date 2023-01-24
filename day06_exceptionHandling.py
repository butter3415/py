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
