class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성되었습니다.')

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.hp, self.attack, self.defence))

    def __getitem__(self, name):
        if name == 'hp':
            return self.hp
        elif name == 'attack':
            return self.attack
        elif name == 'defence':
            return self.defence
        else:
            return "존재하지 않는 키값입니다."

player_a = charactor(10, 20, 30)

print(player_a['hp'])
print(player_a['attack'])
print(player_a['defence'])
print(player_a['mung'])
