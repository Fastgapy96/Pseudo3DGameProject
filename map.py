import pygame
import random

from main import Game

_ = False

mini_map_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, _, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, _, _, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, _, _, 2, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 2],
    [1, _, _, 1, 1, _, _, _, _, _, 1, 2, 2, 2, 2, 1],
    [1, _, _, _, 1, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, 2, 3, 2, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, 1],
    [1, 1, 1, 1, _, 2, 1, 1, 1, 1, 1, 3, 1, 2, _, 2],
    [1, 1, 1, 2, _, 2, 1, 1, 1, 1, 1, 1, 1, 2, _, 2],
    [1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

mini_map_2 =[
    [1, 1, 1, 1, 1],
    [1, _, _, _, 1],
    [1, _, 1, _, 1],
    [1, _, 1, _, 1],
    [1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.mini_map = self.get_mini_map()
        self.world_map = {}
        self.get_map()

    def get_mini_map(self):
        if self.level == 1:    
            return self.place_mini_maps()
        elif self.level == 2:
             return mini_map_2
        else:
            raise ValueError("Invalid level")

    def place_mini_maps(self):
        map_with_embedded = [row.copy() for row in mini_map_1]
      #  self.place_mini_map(map_with_embedded, mini_map_2, (5, 5))
        return map_with_embedded
    
    def place_mini_map(self, base_map, mini_map, position):
        pos_x, pos_y = position
        rows, cols = len(mini_map), len(mini_map[0])
        for j in range(rows):
            for i in range(cols):
                if 0 <= pos_x + i < len(base_map[0]) and 0 <= pos_y + j < len(base_map):
                    base_map[pos_y + j][pos_x + i] = mini_map[j][i]

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
