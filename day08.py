# class & object
# 동사형으로 표현

class Pokemon:
    def __init__(self, name, owner, skills) :   # constructor, 생성자
        self.name = name    # attribute, field, member variable
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 {name} 생성됨.')

    def info(self): # self -> 실행 시점에 객체 자신을 가르킨다.(this)
        """
        포켓몬 정보(주인, 이름, 기술들) 출력
        :return: void
        """
        print(f'{self.owner}의 포켓몬은 {self.name}입니다')
        for skill in self.skills:
            print(f'==========\n{skill}')
        print("==========")


p1 = Pokemon('피카츄', '지우', "번개/백만볼트/전광석화")
p2 = Pokemon('파이리', '지혜', '화염발사/불기둥')
p3 = Pokemon('꼬부기', '지나', '거품/물대포/몸통박치기')

p2.info()
p2.info()
