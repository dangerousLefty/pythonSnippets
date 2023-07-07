class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name} and I'm level {self.level}")

    def play(self):
        self.level += 1


player1 = Player("Harry", 16)
player1.introduce()
player1.play()
print("level: ", player1.level)


player2 = Player("Steve", 12)
player2.introduce()
player2.play()
print("level: ", player2.level)
