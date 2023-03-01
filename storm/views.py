from random import randrange


class Storm:
    def __init__(self):
        self.chance_to_hit = randrange(10, 100, 10)

    def hit_ship(self, ship_hp):
        damage_done_to_ship = ship_hp * (self.chance_to_hit / 100)
        return damage_done_to_ship

    def hit_soldiers(self, soldiers):
        damage_done_to_soldier = soldiers * (self.chance_to_hit / 100)
        return damage_done_to_soldier
