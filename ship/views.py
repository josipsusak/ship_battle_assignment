class Ship:
    """ Creates an instance of a ship with specific name and number of soldiers """

    def __init__(self, num_of_soldiers, name):
        self.ship_hp = 100
        self.num_of_soldiers = num_of_soldiers
        self.name = name

    """ Create ships with stats, based on query parameters"""

    def create_ships(self, number_of_soldiers):
        counter = 1
        ships_data = []
        for soldiers in number_of_soldiers:
            name = "Ship" + " " + str(counter)
            counter += 1
            new_ship = Ship(soldiers, name)
            print(name)
            print(new_ship.num_of_soldiers)
            print(new_ship.ship_hp)
            data = dict(name=name,
                        ship_hp=new_ship.ship_hp,
                        number_of_soldiers=new_ship.num_of_soldiers)
            ships_data.append(data)
        return ships_data

    def __str__(self):
        return self.name

