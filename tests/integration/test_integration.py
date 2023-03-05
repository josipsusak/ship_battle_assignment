class TestIntegration:

    def test_get(self, client):
        response = client.get("http://127.0.0.1:8000/")
        assert response.status_code == 200
        assert "Attention" in response.data

    def test_query_parameters_insert(self, client):
        response = client.get("http://127.0.0.1:8000/?ships=50,20,70")
        assert response.status_code == 200
        assert "Winner is" in response.data
