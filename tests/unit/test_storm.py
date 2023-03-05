from storm.views import Storm


class TestStormView:

    def test_storm_create(self, ship, result_50):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        assert storm.soldiers == result_50
        assert storm.ship_hp == 100

    def test_storm_hit_ship(self, ship, chance_to_hit, result_50):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        storm.chance_to_hit = chance_to_hit
        result = storm.hit_ship()
        assert result == result_50

    def test_storm_hit_soldiers(self, ship, chance_to_hit, result_25):
        storm = Storm(ship[0]["ship_hp"], ship[0]["number_of_soldiers"])
        storm.chance_to_hit = chance_to_hit
        result = storm.hit_soldiers()
        assert result == result_25

    def test_storm_hits(self, ship_integration_test_data, chance_to_hit, result_25, result_50):
        storm = Storm(ship_integration_test_data["ship_hp"], ship_integration_test_data["number_of_soldiers"])
        storm.chance_to_hit = chance_to_hit
        storm_hits = storm.hit_ship()
        ship_integration_test_data.update({"ship_hp": storm_hits})
        storm_hits_soldiers = storm.hit_soldiers()
        ship_integration_test_data.update({"number_of_soldiers": storm_hits_soldiers})
        assert ship_integration_test_data["number_of_soldiers"] == result_25
        assert ship_integration_test_data["ship_hp"] == result_50
