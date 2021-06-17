class charactor:

    def create(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

    def show_info(self):
        print("hp: %d, attack: %d, defence: %d " %(self.hp, self.attack, self.defence))

player_a = charactor()
player_b = charactor()

player_a.create(10, 20, 30)
player_b.create(100, 200, 300)

player_a.show_info()
player_b.show_info()
