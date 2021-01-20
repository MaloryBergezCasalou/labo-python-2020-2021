import random

global board, players
startingMoney = 50


class Cell:
    def __init__(self, cost):
        self.cost = cost


class Board:
    def __init__(self, size):
        self.size = size
        self.create()
        self.show()

    def create(self):
        self.board = []
        for i in range(self.size):
            self.board.append(Cell(random.randint(-5, 5)))

    def show(self):
        global players
        print("".join(["%3s" % str(line.cost) for line in self.board]))
        for i in range(len(self.board)):
            print("%3s" % "".join(
                [player.playerId if player.pos == i else "" for player in players]), end="")
        print("")


class Player:
    def __init__(self, playerId):
        self.pos = 0
        self.loose = False
        self.money = startingMoney
        self.playerId = playerId
        self.show()

    def show(self):
        pass

    def move(self):
        global board
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.pos = (self.pos + (dice1 + dice2)) % board.size
        self.money += board.board[self.pos].cost
        print(
            f"Le joueur {self.playerId} a fait {dice1} et {dice2} = {dice1+dice2}. Il possède maintenant {self.money}$")
        board.show()
        if self.money < 1:
            self.loose = True
            print(f"le joueur {self.playerId} a perdu :(")
        if dice1 == dice2:
            print("Le joueur a fait deux fois le même chiffre donc il rejoue !")
            self.move()


def main():
    global board, players
    players = []
    players.append(Player("A"))
    players.append(Player("B"))
    board = Board(40)
    inGame = True
    while inGame:
        if inGame:
            players[0].move()
        if players[0].loose:
            inGame = False
        if inGame:
            players[1].move()
        if players[1].loose:
            inGame = False


if __name__ == "__main__":
    main()
