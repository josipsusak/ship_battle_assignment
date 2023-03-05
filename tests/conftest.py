import pytest


@pytest.fixture
def ship():
    data = [{'name': 'Ship 1', 'ship_hp': 100, 'number_of_soldiers': 50},
            {'name': 'Ship 2', 'ship_hp': 100, 'number_of_soldiers': 70},
            {'name': 'Ship 3', 'ship_hp': 100, 'number_of_soldiers': 90}
            ]
    return data


@pytest.fixture
def chance_to_hit():
    chance_to_hit = 50
    return chance_to_hit


@pytest.fixture
def result_25():
    result_25 = 25
    return result_25


@pytest.fixture
def result_50():
    result_50 = 50
    return result_50


@pytest.fixture
def number_of_soldiers_by_ship():
    data = [50, 70, 90]
    return data


@pytest.fixture
def ship_integration_test_data():
    data = {'name': 'Ship 1', 'ship_hp': 100, 'number_of_soldiers': 50}
    return data
