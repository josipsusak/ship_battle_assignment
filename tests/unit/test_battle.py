from battle.views import Battle


class TestBattleView:

    def test_homepage(self, client):
        response = client.get("http://127.0.0.1:8000/")
        assert response.status_code == 200
        assert "Attention" in response.data

    def test_calculate_result(self, ship):
        battle = Battle()
        result = battle.calculate_result(ship)
        assert "Ship 3" in result
        assert "Ship 2" not in result
        assert "Ship 1" not in result


