import numpy as np
import matplotlib.pyplot as plt
from ypsrtuct import structure
import ga

#sphere test function
def sphere(x):
    return sum(x**2)

    #problem definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA Parameter
params = structure()
param.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 0.1

# Run GA
out = ga.run(problem, params)

# Result

