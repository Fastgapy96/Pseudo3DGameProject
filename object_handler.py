from sprite_object import *
from npc import *

class ObjectHandler():
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/soldier'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #sprite map
        add_sprite(AnimatedSprites(game))
        add_sprite(AnimatedSprites(game, pos=(1.5, 1.5)))

        #npc map
        add_npc(SoldierNPC(game, pos=(10.5, 3.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 5.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)    

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)    