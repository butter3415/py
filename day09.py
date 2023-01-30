# Pokemon game v0.2

class Pokemon:
    def __init__(self, owner, skills):  # constructor
        self.__owner = owner  # like private
        self.skills = skills.split('/')  # list
        import datetime  # 상속관계 x
        print(f'[{datetime.datetime.now()}] 포켓몬 생성됨 :', end=' ')

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def info(self):  # method (member function)
        """
        포켓몬 정보(주인, 이름, 기술들) 출력
        :return: void
        """
        print(f'{self.__owner}의 포켓몬이 사용 가능한 스킬')
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):  # class 자식클래스(부모클래스):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'[삐까삐까] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')


class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')


class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'[파읠파읠] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')


if __name__ == "__main__":
    while True:
        menu = input('1) 포켓몬 생성  2) 프로그램 종료 : ')
        if '2' == menu:
            print('프로그램을 종료합니다')
            break
        elif '1' == menu:
            pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리 : ')
            n = input('플레이어 이름 입력 : ')
            ss = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
            if pokemon == '1':
                p = Pikachu(n, ss)
            elif pokemon == '2':
                p = Ggoboogi(n, ss)
            elif pokemon == '3':
                p = Pairi(n, ss)
            else:
                continue
            p.info()  # skill selection
            attack_no = int(input('공격 번호 선택 : '))
            p.attack(attack_no-1)
        else:
            print('메뉴에서 골라 주세요')