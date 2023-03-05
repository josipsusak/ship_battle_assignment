from famine.views import Famine


class TestFamineView:

    def test_famine_create(self, ship, result_50):
        famine = Famine(ship[0]["number_of_soldiers"])
        assert famine.soldiers == result_50

    def test_famine_hit_soldiers(self, ship, chance_to_hit, result_25):
        famine = Famine(ship[0]["number_of_soldiers"])
        famine.chance_to_hit = chance_to_hit
        result = famine.hit_soldiers()
        assert result == result_25

    def test_famine_hits(self, ship_integration_test_data, chance_to_hit, result_25):
        famine = Famine(ship_integration_test_data["number_of_soldiers"])
        famine.chance_to_hit = chance_to_hit
        famine_hits = famine.hit_soldiers()
        ship_integration_test_data.update({"number_of_soldiers": famine_hits})
        assert ship_integration_test_data["number_of_soldiers"] == result_25
