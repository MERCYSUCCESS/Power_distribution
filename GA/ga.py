from copy import deepcopy
from math import gamma
import numpy as np
from ypstruct import structure

def run(problem, params):

# problem information
costfunc = problem.costfunc
nvar = problem.nvar
varmin = problem.varmin
varmax = problem.varmax

# parameters
maxit = params.maxit
npop = params.npop
pc = params.pc
nc = np.round(pc*npop/2)*2
gamma = params.gamma
 
 # Empty Individual Template
 empty_individual = structure()
 empty_individual.position = None
 empty_individual.cost = None

 #BestSolution Ever
 bestsol = empty_individual.deepcopy()
 bestsol.cost = np.inf


# initialize population
pop = empty_individual.repeat(npop)
for i in range(0, npop):
    pop[i].position = np.random.uniform(varmin, varmax, nvar)
    pop[i].cost = costfunc(pop[i].position)
    if pop[i].cost < bestsol.cost:
        bestsol = pop[i].deepcopy()

        # Best Cost of Iteration
        bestcost = np.empty(maxit)

        #main Loop
        for it in range(maxit): 

            popc = []
            for k in range(nc//2):

                #select parent
                q = np.random.permutation(npop)
                p1 = pop[q[0]]
                p2 = pop[q[1]]

                # perform crossover
                c1, c2 = crossover(p1,p2, gamma)

                # Perform Mutation
                c1 = mutate(c1, mu, sigma)
                c2 = mutate(c2, mu, sigma)



    # Output
    out = structure()
    out.pop = pop
    return out

def crossover(p1,p2, gamma=0.1):
    c1 = p1.deepcopy()
    c2 = p1.deepcopy()
    alpha = np.random.uniform(-gamma, 1+gamma *c1.posittion.shape)
    c1.position = alpha*p1.position + (1-alpha)*p2.position
    c2.position = alpha*p2.position + (1-alpha)*p1.position
    return c1, c2

def mutate(x, mu, sigma):
    y = x.deepcopy()
    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)
    y.position[ind] = x.position[ind] + sigma*np.random.randn()





    #output
    out = source ()
    out.pop = pop
    return out