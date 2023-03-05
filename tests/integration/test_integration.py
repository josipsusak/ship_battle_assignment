class TestIntegration:

    # Tests if get method is working, asserting "Attention" as it's only in response when get method is valid
    def test_get(self, client):
        response = client.get("http://127.0.0.1:8000/")
        assert response.status_code == 200
        assert "Attention" in response.data

    # Tests if app is working when proper query parameters are input, asserting "Winner is...", because it's only
    # inside of response if app is working properly and results are calculated
    def test_query_parameters_insert(self, client):
        response = client.get("http://127.0.0.1:8000/?ships=50,20,70")
        assert response.status_code == 200
        assert "Winner with the highest ship HP and number of solders is" in response.data
