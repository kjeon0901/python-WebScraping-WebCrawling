class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성되었습니다.')

player_a = charactor(10, 20, 30)
player_b = charactor(100, 200, 300)


print(player_a.hp)
print(player_a.attack)
print(player_a.defence)
print(player_b.hp)
print(player_b.attack)
print(player_b.defence)
