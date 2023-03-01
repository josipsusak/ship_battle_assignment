from random import randint


class Storm:
    def __init__(self):
        self.chance_to_hit = randint(1, 4)

    def hit_ship(self, ship_hp):
        damage_done_to_ship = ship_hp * (self.chance_to_hit / 100)
        return damage_done_to_ship

    def hit_soldiers(self, soldier_hp):
        damage_done_to_soldier = soldier_hp * (self.chance_to_hit / 100)
        return damage_done_to_soldier
