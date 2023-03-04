from ship.views import Ship


class TestShipView:

    def test_ship_create(self, ship):
        ship = Ship(ship[1]["number_of_soldiers"], ship[1]["name"])
        assert ship.name == "Ship 2"
        assert ship.num_of_soldiers == 70

    def test_create_ships(self, number_of_soldiers_by_ship):
        ship = Ship()
        result = ship.create_ships(number_of_soldiers_by_ship)
        assert result is type(list)
