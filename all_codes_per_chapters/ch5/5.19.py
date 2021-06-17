class charactor:

    def __init__(self, hp, attack, defence):
        self.info = {
            'hp': hp,
            'attack': attack,
            'defence': defence,
        }

        print('player가 생성되었습니다.')

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.info['hp'], self.info['attack'], self.info['defence']))

    def __getitem__(self, name):
        if name in self.info.keys():
            return self.info[name]
        else:
            return "존재하지 않는 키값입니다."

player_a = charactor(10, 20, 30)
player_b = charactor(100, 200, 300)

print(player_a['hp'])
print(player_a['attack'])
print(player_a['defence'])
print(player_a['mung'])
