from storm.views import Storm


class TestStormView:

    def test_storm_create(self, ship):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        assert storm.soldiers == 50
        assert storm.ship_hp == 100

    def test_storm_hit_ship(self, ship):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        storm.chance_to_hit = 50
        result = storm.hit_ship()
        assert result == 50

    def test_storm_hit_soldiers(self, ship):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        storm.chance_to_hit = 50
        result = storm.hit_soldiers()
        assert result == 25
