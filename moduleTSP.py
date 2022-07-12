import numpy as np
import random as rn

# INITIALIZATION POPULATION
def create_population(matrix_size):
    # container is used to store the population
    container = []
    for x in range(matrix_size[0]):
        population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # shuffling the population to create an initial population matrix in random
        # and there will be no same number in one chromosome
        np.random.shuffle(population)
        container.append(population)
    return container

# FITNESS EVALUATION
def fitness_route(route, population):
    # function to get the total distance in population
    # and use it as a sample to find the fitness value
    container = []
    for pop in population:
        total = []
        i = 1
        for sub_pop in pop:
            if i == 10:
                i = 9
            print("\nChromosome: ", pop)
            print("First: ", sub_pop)
            print("Second: ", pop[i])
            for x in route:
                if x[0] == sub_pop:
                    if x[1] == pop[i]:
                        print("Data: ", x)
                        print("Distance: ", x[2])
                        total.append(x[2])
            i = i + 1

        total = np.sum(total)
        print("\nTotal Distance: ", total)
        container.append(total)

    return container

def shortest_parents(population, fitness):
    # FITNESS EVALUATION
    # fitness is used as a number counter
    fitnes = []
    # calculate the fitness value by
    # inversing the sample or the total distance
    # in each chromosome in population
    # (1/total distance each chromosome)
    for sample in fitness:
        q = 1/sample
        fitnes.append(q)
    print("\nDistance: \n", fitness)

    total = 0
    # then the results of all fitness value will be totaled
    for q in fitnes:
        print("\nFitness Value: ", q)
        total = total + q
    print("\nTotal Fitness Value: ", total)

    probability = []
    # calculate the probability value
    for q in fitnes:
        total = q / total
        probability.append(total)
    print("\nProbability Value: \n", probability)

    cumulativeVal = []
    # calculate the cumulative value
    total = 0
    for cumulative in probability:
        total = total + cumulative
        cumulativeVal.append(total)
    print("\nCumulative Value: \n", cumulativeVal)


    # SELECTION INDIVIDUAL
    # from the cumulative value results
    # we will make limitations for the Roulette Wheel
    # Individual Selection to get the best individual in population
    # as a parents to do reproduction
    i = 0
    new_population = population
    print("\nPopulation Before Roulette Wheel: \n", new_population)

    # SELECTION INDIVIDUAL (ROULETTE WHEEL)
    # it will loop as much as the number of chromosomes
    for x in cumulativeVal:
        best_cumulativeVal = np.max(cumulativeVal)
        print("\nBest Cumulative Value: ", best_cumulativeVal)

        # it will take random numbers and this random number will
        # be used as a modifier of the-x chromosome when looping
        # with the-x population chromosome
        r = np.random.uniform(0, best_cumulativeVal)
        print("Random Value: ", r)

        # it will form a new population on the condition
        # that the random number must be less than x
        if r < x:
            print("\nLooping: ", i)
            print("Entering")
            if r <= cumulativeVal[0]:
                print("0th Chromosome")
                new_population[i] = population[0]
            elif cumulativeVal[0] > r and r <= cumulativeVal[1]:
                print("1st Chromosome")
                new_population[i] = population[1]
            elif cumulativeVal[1] > r and r <= cumulativeVal[2]:
                print("2nd Chromosome")
                new_population[i] = population[2]
            elif cumulativeVal[2] > r and r <= cumulativeVal[3]:
                print("3rd Chromosome")
                new_population[i] = population[3]
            elif cumulativeVal[3] > r and r <= cumulativeVal[4]:
                print("4th Chromosome")
                new_population[i] = population[4]
            elif cumulativeVal[4] > r and r <= cumulativeVal[5]:
                print("5th Chromosome")
                new_population[i] = population[5]
            elif cumulativeVal[5] > r and r <= cumulativeVal[6]:
                print("6th Chromosome")
                new_population[i] = population[6]
            elif cumulativeVal[6] > r and r <= cumulativeVal[7]:
                print("7th Chromosome")
                new_population[i] = population[7]
            elif cumulativeVal[7] > r and r <= cumulativeVal[8]:
                print("8th Chromosome")
                new_population[i] = population[8]
            elif cumulativeVal[8] > r and r <= cumulativeVal[9]:
                print("9th Chromosome")
                new_population[i] = population[9]

        i = i + 1
    # create a new population after roulette wheel
    # to be a parents to do reproduction
    new_population = np.array(new_population)
    print("\nPopulation After Roulette Wheel: \n", new_population)

    return new_population


# REPRODUCTION: CROSS-OVER
def population_crossover(parents):
    offspring = parents
    print("\nParents: \n", parents)

    i = 0
    parentsLength = len(parents)
    parentsLength = int(parentsLength / 2)

    # in this population crossover we will
    # randomize a number from 0 to (length of parents - 1)
    # in here the length of the parents is 10, meaning 10-1 = 9
    # so, we can say random numbers from 0-9
    for a in range(parentsLength):
        r = rn.randint(0, parentsLength - 1)
        print("\nGene Position:", r)
        child1 = parents[i, r]
        child2 = parents[i + 1, r]
        print("1st Child: ", child1)
        print("2nd Child: ", child2)
        print("1st Offspring Before: ", parents[i])
        print("2nd Offspring Before: ", parents[i + 1])

        # change child row in offspring
        # check the same gene/number in chromosome
        first = np.where(parents[i] == child2)
        second = np.where(parents[i + 1] == child1)

        # the working principle of crossover is to take each gene
        # on two chromosomes and then exchange the gene according to
        # the position obtained from a random number, and if there is
        # the same gene/number on one chromosome, the gene must also be
        # exchanged in order to keep getting a different gene/number on
        # each chromosome
        first = np.array(first)
        first = first[0][0]
        second = np.array(second)
        second = second[0][0]
        print("1st Same Gene Position: ", first)
        print("2nd Same Gene Position: ", second)

        parents[i, first] = child1
        parents[i, r] = child2
        parents[i+1, second] = child2
        parents[i+1, r] = child1
        print('----------------------------------------------------------------------')
        print("1st Offspring After: ", parents[i])
        print("2nd Offspring After: ", parents[i + 1])
        i = i + 2

    return parents


# REPRODUCTION: MUTATION
def population_mutation(crossover):
    offspring = crossover
    i = 0
    for chromosome in crossover:
        # in the mutation itself, we exchange the x-th gene
        # with the x-th gene + 1 and its position will be
        # obtained randomly as well
        print("\nChromosome Before: \n", chromosome)
        r = rn.randint(0, 8)
        print("Gene Position: ", r)
        print("1st Child: ", chromosome[r])
        print("2nd Child: ", chromosome[r + 1])
        print("Offspring: ", chromosome)

        child1 = chromosome[r]
        child2 = chromosome[r + 1]
        offspring[i, r] = child2
        offspring[i, r + 1] = child1
        print("Offspring After Mutation: ", offspring[i])
        print("Chromosome After: \n", offspring[i])
        i = i + 1

    return crossover
