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
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(6.5, 14.75)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 16.75)))
        add_sprite(AnimatedSprite(game, pos=(1.3, 11.1)))
        add_sprite(AnimatedSprite(game, pos=(1.1, 18.7)))
        add_sprite(AnimatedSprite(game, pos=(3.8, 14.4)))

        #npc map
        add_npc(SoldierNPC(game, pos=(10.5, 3.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 5.5)))
        add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        add_npc(SoldierNPC(game, pos=(5.5, 14.5)))
        add_npc(SoldierNPC(game, pos=(7.5, 12.5)))
        add_npc(CyberDemon(game, pos=(11.5, 15.5)))
        add_npc(SoldierNPC(game, pos=(14.0, 2.5)))
        add_npc(SoldierNPC(game, pos=(12.75, 11.45)))
        add_npc(SoldierNPC(game, pos=(13.1, 11.8)))
        add_npc(SoldierNPC(game, pos=(13.5, 18.0)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)    

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)    