from famine.views import Famine


class TestFamineView:

    def test_famine_create(self, ship):
        famine = Famine(ship[0]["number_of_soldiers"])
        assert famine.soldiers == 50

    def test_famine_hit_soldiers(self, ship):
        famine = Famine(ship[0]["number_of_soldiers"])
        famine.chance_to_hit = 50
        result = famine.hit_soldiers()
        assert result == 25
