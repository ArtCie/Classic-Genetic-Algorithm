from algorithm.population_repository import PopulationRepository

import pytest

POPULATION_SIZE = 20


@pytest.fixture
def population() -> PopulationRepository:
    return PopulationRepository(-10, 10, 6, POPULATION_SIZE)


class TestPopulation:
    def test_chromosome_length(self, population: PopulationRepository):
        assert population._get_chromosome_length() == 25

    def test_populate(self, population: PopulationRepository):
        assert len(population.population) == POPULATION_SIZE
