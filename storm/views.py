from random import randrange


class Storm:
    """Creates an instance of a storm to hit both soldiers and ships, damaging both"""

    def __init__(self, ship_hp, soldiers):
        self.chance_to_hit = randrange(10, 100, 10)
        self.ship_hp = ship_hp
        self.soldiers = soldiers

    def hit_ship(self):
        damage_done_to_ship = self.ship_hp * (self.chance_to_hit / 100)
        hp_after_storm = int(self.ship_hp - damage_done_to_ship)
        return hp_after_storm

    def hit_soldiers(self):
        soldiers_killed = self.soldiers * (self.chance_to_hit / 100)
        soldiers_alive = int(self.soldiers - soldiers_killed)
        return soldiers_alive
