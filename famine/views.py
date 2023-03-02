from random import randrange


class Famine:
    def __init__(self, soldiers):
        self.chance_to_hit = randrange(10, 100, 10)
        self.soldiers = soldiers

    def hit_soldiers(self):
        soldiers_starved = self.soldiers * (self.chance_to_hit / 100)
        soldiers_alive_after_famine = int(self.soldiers - soldiers_starved)
        return soldiers_alive_after_famine
