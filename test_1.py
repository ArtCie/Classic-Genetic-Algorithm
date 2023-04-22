from algorithm.individual import Individual
from algorithm.chromosome import Chromosome
from algorithm.population_repository import PopulationRepository
from algorithm.cross.cross import CrossTypes
from functions.eggholder_function_calculator import EggholderFunctionCalculator
from functions.function_handler import FunctionHandler
from algorithm.selection.selection import SelectionTypes
from algorithm.mutation.mutation import MutationTypes
import numpy as np

population_1 = PopulationRepository(-10.0, 10.0, 6, 12)


decoded_pop = population_1.decode_population()
is_max = 0


func_handler = FunctionHandler(EggholderFunctionCalculator(), is_reversed=not is_max)
function_values = np.array(list(map(func_handler.evaluate, decoded_pop)))

# print(population_1.decode_population())
print("---",function_values)
# for chromosom in population_1.population:
#     print("--------------")
#     print(chromosom.chromosome_1.value)
#     print("*****")
#     print(chromosom.chromosome_2.value)
#     print("--------------")


selection_method = SelectionTypes.get_selection_by_type(2, 3)
selection_method.evaluate(population_1, function_values)

decoded_pop = population_1.decode_population()

function_values = np.array(list(map(func_handler.evaluate, decoded_pop)))
print("---",function_values)

print(population_1)
cross_method = CrossTypes.get_cross_by_type(2,1)
cross_method.evaluate(population_1)

mutation_method = MutationTypes.get_mutation_by_type(2, 0.5)
mutation_method.evaluate(population_1)

# print(population_1.decode_population())
decoded_pop = population_1.decode_population()

function_values = np.array(list(map(func_handler.evaluate, decoded_pop)))
print("---",function_values)

# for chromosom in population_1.population:
#     print("--------------")
#     print(chromosom.chromosome_1.value)
#     print("*****")
#     print(chromosom.chromosome_2.value)
#     print("--------------")