class charactor:
    char_cnt = 0

    def __init__(self, hp, attack, defence):
        self.info = {
            'hp': hp,
            'attack': attack,
            'defence': defence,
        }

        charactor.char_cnt += 1

        print('player가 생성되었습니다. 생성된 유닛 수 : %d' %(charactor.char_cnt))

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.info['hp'], self.info['attack'], self.info['defence']))

    def __del__(self):
        charactor.char_cnt -= 1
        print('player가 제거됬었습니다. 생성된 유닛 수 : %d' %(charactor.char_cnt))

player_a = charactor(10, 20, 30)
player_b = charactor(100, 200, 300)
player_c = charactor(100, 200, 300)
player_d = charactor(100, 200, 300)
player_e = charactor(100, 200, 300)

del player_c

print('program end')
