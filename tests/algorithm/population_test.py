from algorithm.population import Population

import pytest

POPULATION_SIZE = 20


@pytest.fixture
def population() -> Population:
    return Population(-10, 10, 6, POPULATION_SIZE)


class TestPopulation:
    def test_chromosome_length(self, population: Population):
        assert population._get_chromosome_length() == 25

    def test_populate(self, population: Population):
        assert len(population.population) == POPULATION_SIZE
