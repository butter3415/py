# class & object
# 동사형으로 표현

class Pokemon:
    def __init__(self, owner, skills) :   # constructor, 생성자
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성됨 :', end = ' ')

    def info(self): # self -> 실행 시점에 객체 자신을 가르킨다.(this)
        """
        포켓몬 정보(주인, 이름, 기술들) 출력
        :return: void
        """
        print(f'{self.owner}의 포켓몬은 {self.name}입니다')
        for skill in self.skills:
            print(f'==========\n{skill}')
        print("==========")

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!!!')

class Pikachu(Pokemon): # class 자식클래스(부모클래스):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)     # 부모 코드 가져와야 실행 가능
        self.name = "피카츄"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[피까피까] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')
        

class Ggobboogi(Pokemon):    # inheritance(상속)
    def __init__(self, owner, skills):
        super().__init__(owner, skills)     # 부모 코드 가져와야 실행 가능
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')

pika1 = Pikachu('지혜', '번개/백만볼트')
ggo1 = Ggobboogi('오바람', '거품/물대포/몸통박치기')
# print(pika1.owner)
# pika1.info()
pika1.attack(1)
ggo1.attack(2)
