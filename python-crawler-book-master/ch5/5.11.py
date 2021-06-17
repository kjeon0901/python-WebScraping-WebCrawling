class charactor:

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

player_a = charactor()
player_b = charactor()

player_a.move()
player_b.move()
