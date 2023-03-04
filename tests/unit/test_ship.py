from ship.views import Ship


class TestShipView:

    def test_create_ships(self, number_of_soldiers_by_ship):
        result = Ship().create_ships(number_of_soldiers_by_ship)
        assert result[0]["name"] == "Ship 1"
        assert result[2]["number_of_soldiers"] == 90
