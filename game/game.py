import random


class Tile:

    def __init__(self, type='E', contain=set()) -> None:
        self.type = type
        self.contain = contain
    
    def set_type(self, type) -> None:
        self.type = type
    
    def add(self, item) -> None:
        self.contains.add(item)
    
    def contains(self) -> set:
        return self.contain
    
    def remove(self, item) -> None:
        self.contain.remove(item)

class Map:

    def __init__(self) -> None:
        self.map = [[Tile() for _ in range(4)] for __ in range(4)]
        i, j = self.random_i_j()
        while i == 0 and j == 0:
            i, j = random.randint(0, 3), random.randint(0, 3)
        self.map[i][j].set_type('W')
        self.fill_adjacent(i, j, 'stench')

        i, j = self.random_i_j()
        self.map[i][j].add('gold')

        self.map[0][0].add('player')

    # TODO add moving and checks, losing and wining
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
        if i - 1 >= 0:
            if j - 1 >= 0:
                self.map[i-1][j-1].add(item)
            if n > j + 1:
                self.map[i-1][j+1].add(item)
        if i + 1 > n:
            if j - 1 >= 0:
                self.map[i+1][j-1].add(item)
            if n > j + 1:
                self.map[i+1][j+1].add(item)