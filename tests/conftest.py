import pytest


@pytest.fixture
def ship():
    data = [{'name': 'Ship 1', 'ship_hp': 100, 'number_of_soldiers': 50},
            {'name': 'Ship 2', 'ship_hp': 100, 'number_of_soldiers': 70},
            {'name': 'Ship 3', 'ship_hp': 100, 'number_of_soldiers': 90}
            ]
    return data


@pytest.fixture
def number_of_soldiers_by_ship():
    data = [50, 70, 90]
    return data
