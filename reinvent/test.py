import sys
from scoring_functions import get_scoring_function

sf = get_scoring_function('activity_model2', num_processes=0)
score = sf("c1ccc2c(c1)C(=O)N(c3ccc(cc3S2)NC(=O)[C@H]4CC(=O)N(C4)c5cccc(c5)Cl)C6CC6")

print(len(score))
print(score)
