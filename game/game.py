import random


class Tile:

    def __init__(self, type='E', contain=None) -> None:
        self.type = type
        if contain is not None:
            self.contain = contain
        else:
            self.contain = []

    def set_type(self, type) -> None:
        self.type = type

    def add(self, item) -> None:
        if item not in self.contain:
            self.contain.append(item)

    def contains(self) -> list:
        return self.contain

    def remove(self, item) -> None:
        self.contain.remove(item)


class Map:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    WIN = "WIN"
    LOSS = "LOSS"

    def __init__(self, difficulty='easy') -> None:
        self.map = []
        self.visited = []
        self.player = (0, 0)
        self.gold_picked_up = False
        self.size = 4
        self.done = False
        self.difficulty = difficulty
        self.init()

    def init(self):
        self.map = [[Tile() for _ in range(self.size)] for __ in range(self.size)]
        self.visited = [[False for _ in range(self.size)] for __ in range(self.size)]

        i, j = self.random_i_j()
        while i == 0 and j == 0:
            i, j = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.map[i][j].set_type('wumpus')

        self.fill_adjacent(i, j, 'stench')

        i, j = self.random_i_j()
        self.map[i][j].add('gold')
        self.gold_picked_up = False

        self.player = (0, 0)
        self.map[0][0].add('player')
        self.visited[0][0] = True

        self.done = False

    # TODO add moving and checks, losing and wining
    def move(self, direction):
        if not self.done:

            if self.bonk(direction):
                return "BONK"

            px, py = self.player
            self.map[px][py].remove('player')

            px, py = px + direction[0], py + direction[1]
            self.player = (px, py)
            tile = self.map[px][py]
            self.visited[px][py] = True
            tile.add('player')

            if px == py == 0 and self.gold_picked_up:
                self.done = True
                return Map.WIN

            in_tile = tile.contains()
            if 'wumpus' == tile.type:
                self.done = True
                return Map.LOSS
            if 'gold' in in_tile:
                tile.remove('gold')
                self.gold_picked_up = True
                return in_tile + ['gold']
            return in_tile

    def bonk(self, direction) -> bool:
        n = len(self.map)
        px, py = self.player
        dx, dy = direction

        if px + dx < 0 or px + dx >= n:
            return True
        if py + dy < 0 or py + dy >= n:
            return True
        return False

    # TODO
    # add pits, and breezes
    # add crossbow
    # add score   

    def random_i_j(self):
        i, j = random.randint(0, 3), random.randint(0, 3)
        while i == 0 and j == 0:
            i, j = random.randint(0, 3), random.randint(0, 3)
        return i, j

    def fill_adjacent(self, i, j, item):
        n = len(self.map)

        if i > 0:
            self.map[i - 1][j].add(item)
        if i + 1 < n:
            self.map[i + 1][j].add(item)

        if j > 0:
            self.map[i][j - 1].add(item)
        if j + 1 < n:
            self.map[i][j + 1].add(item)


if __name__ == '__main__':
    map = Map()
    for row in map.map:
        for tile in row:
            pass
            # print(tile.contains())
