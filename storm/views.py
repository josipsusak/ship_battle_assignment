from random import randrange


class Storm:
    def __init__(self):
        self.chance_to_hit = randrange(10, 100, 10)

    def hit_ship(self, ship_hp):
        damage_done_to_ship = ship_hp * (self.chance_to_hit / 100)
        hp_after_storm = ship_hp - damage_done_to_ship
        return hp_after_storm

    def hit_soldiers(self, soldiers):
        soldiers_killed = soldiers * (self.chance_to_hit / 100)
        soldiers_alive = soldiers - soldiers_killed
        return soldiers_alive
