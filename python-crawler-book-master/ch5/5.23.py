class unit:
    unit_cnt = 0

    def __init__(self):
        print('unit 생성')
        unit.unit_cnt += 1

    def move(self):
        print('unit move')


class bird(unit):
    def __init__(self):
        print('bird 생성')
        super(bird, self).__init__()


class ground(unit):
    def __init__(self):
        print('ground 생성')
        super(ground, self).__init__()

b1 = bird()
b3 = bird()

b1.move()

g1 = ground()

print(unit.unit_cnt)
