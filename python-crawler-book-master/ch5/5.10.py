class charactor:
    def move(self):
        print(self, 'move')

    def attack(self):
        print(self, 'attack')

player_a = charactor()
player_b = charactor()

player_a.move()
player_a.attack()
player_b.move()
player_b.attack()
