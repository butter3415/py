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

class Pikachu(Pokemon): # class 자식클래스(부모클래스):
    pass

pika1 = Pikachu('피카츄', '지혜', '번개/백만볼트/천만볼트/전광석화')
pika1.info()
p1 = Pokemon('파이리','지혜','화염발사/불기둥')
p1.info()