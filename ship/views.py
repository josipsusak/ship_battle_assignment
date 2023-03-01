class Ship:
    """ Creates an instance of a ship with specific name and number of soldiers """

    def __init__(self, num_of_soldiers):
        self.ship_hp = 100
        self.num_of_soldiers = num_of_soldiers
        self.name = ""

    def __str__(self):
        return self.name
