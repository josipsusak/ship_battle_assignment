class Ship:
    """ Creates an instance of a ship with specific name and number of soldiers """

    def __init__(self):
        self.ship_hp = 100
        self.name = "Ship"

    def create_ships(self, number_of_soldiers):
        counter = 1
        ships_data = []
        for soldiers in number_of_soldiers:
            self.name = "Ship" + " " + str(counter)
            counter += 1
            data = dict(name=self.name,
                        ship_hp=self.ship_hp,
                        number_of_soldiers=soldiers)
            ships_data.append(data)
        return ships_data
