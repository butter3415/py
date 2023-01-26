class Pokemon :

    def __init__(self):
            pokemonName = int(input('1) 피카츄 2) 꼬부기 3) 파이리 : '))
            if  pokemonName == 1 :
                self.name = '피카츄'
                self.cry = '피까피까'
            elif pokemonName == 2 :
                self.name = '꼬부기'
                self.cry = '꼬북꼬북'
            elif pokemonName == 3 :
                self.name = '파이리'
                self.cry = '파읠파읠'

            self.owner = input('플레이어 이름 입력 : ')
            skill = str(input('사용 가능한 기술 입력(/로 구분하여 입력) : '))
            self.skills = skill.split('/')
            print(f'포켓몬 생성 : {self.name}')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬')

        i = 0
        for skill in self.skills:
            print(f'{i+1} : {skill}')
            i += 1

    def attack(self):
        skill = int(input('공격 번호 선택 : '))
        print(f'[{self.cry}] {self.owner}의 {self.name}가 {self.skills[skill-1]} 공격 시전!')


while True:
    StartSet = int(input('1) 포켓몬 생성 2) 프로그램 종료 : '))
    if StartSet == 1:
        p1 = Pokemon()
        p1.info()
        p1.attack()
    elif StartSet == 2:
        print('프로그램 종료!')
        break
    else:
        print('메뉴에서 골라주세요')


