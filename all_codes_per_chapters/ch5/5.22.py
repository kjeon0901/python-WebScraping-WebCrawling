class unit:
    unit_count = 0

    def __init__(self):
        print('unit 생성')
        unit.unit_count += 1

    def move(self):
        print('unit move')


class bird(unit):
    def __init__(self):
        print('bird 생성')


class ground(unit):
    def __init__(self):
        print('ground 생성')

b1 = bird()
b2 = bird()
b3 = bird()

b1.move()
print(unit.unit_count)
