class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성되었습니다.')

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

    def show_info(self):
        print("hp: %d, attack: %d, defence: %d " %(self.hp, self.attack, self.defence))

    def __del__(self):
        print('player가 죽었습니다.')

player_a = charactor(10, 20, 30)
player_b = charactor(100, 200, 300)
player_c = charactor(100, 200, 300)

player_a.show_info()
player_b.show_info()
player_c.show_info()

del player_a
del player_b

print("=====program end========")
