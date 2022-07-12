import numpy as np
import moduleTSP as mdl
import matplotlib.pyplot as plt

# Implement of Genetic Algorithm in the Shortest Route Case
# M-IT 2020 Class 3
# Mulya Fajar Ningsih Alwi (001202000101)

# route data sampling
# each data includes:
# 1st num = origin city
# 2nd num = destination city
# 3rd num = distance
route = np.array([
    [1,2,20],[1,3,40],[1,4,60],[1,5,80],[1,6,100],[1,7,120],[1,8,140],[1,9,160],[1,10,180],
    [2,1,20],[2,3,220],[2,4,240],[2,5,260],[2,6,280],[2,7,300],[2,8,320],[2,9,340],[2,10,360],
    [3,1,40],[3,2,220],[3,4,380],[3,5,400],[3,6,420],[3,7,440],[3,8,460],[3,9,480],[3,10,500],
    [4,1,60],[4,2,240],[4,3,380],[4,5,520],[4,6,540],[4,7,560],[4,8,580],[4,9,600],[4,10,620],
    [5,1,80],[5,2,260],[5,3,400],[5,4,520],[5,6,640],[5,7,660],[5,8,680],[5,9,700],[5,10,720],
    [6,1,100],[6,2,280],[6,3,420],[6,4,540],[6,5,640],[6,7,740],[6,8,760],[6,9,780],[6,10,800],
    [7,1,120],[7,2,300],[7,3,440],[7,4,560],[7,5,660],[7,6,740],[7,8,820],[7,9,840],[7,10,860],
    [8,1,140],[8,2,320],[8,3,460],[8,4,580],[8,5,680],[8,6,760],[8,7,820],[8,9,880],[8,10,900],
    [9,1,160],[9,2,340],[9,3,480],[9,4,600],[9,5,700],[9,6,780],[9,7,840],[9,8,880],[9,10,920],
    [10,1,180],[10,2,360],[10,3,500],[10,4,620],[10,5,720],[10,6,800],[10,7,860],[10,8,900],[10,9,920]
    ])

# INITIALIZATION POPULATION
num_of_individuals = 10
num_of_population = 6
matrix_size = (num_of_individuals, num_of_population)
num_of_generations = 20

# create population using the matrix_size
population = mdl.create_population(matrix_size)
population = np.array(population)
print("\nInitial Population: \n", population)

# FITNESS EVALUATION
# get the initial best fitness value
fitness = mdl.fitness_route(route, population)
print("\nInitial Distance: \n", fitness)
# calculate the best fitness value by looking for the minimum value
# because what we are looking for is the shortest route
best_fitness = np.where(fitness == min(fitness))
best_fitness = best_fitness[0][0]
# get the best fitness value by inversing the best total distance
# (1/best distance)
print("\nInitial Best Fitness: ", 1 / (fitness[best_fitness]))

# create the initial shortest route graphic
plt.title('Initial Shortest Route')
plt.ylabel('Population')
plt.xlabel('Fitness')
plt.plot(population[best_fitness], fitness, marker='o', linewidth=4, markersize=12, linestyle='-', color='red')
plt.show()


for x in range(num_of_generations):
    print("\nGenerations: ", x)
    fitness = mdl.fitness_route(route, population)

    parents = mdl.shortest_parents(population, fitness)

    # get the best fitness value from parents by inversing
    # the best total distance (1/best distance)
    parents_fitness = mdl.fitness_route(route, parents)
    print("\nParents Distance: \n", parents_fitness)
    print("\nParents Best Fitness: ", 1 / (fitness[best_fitness]))

    # get the crossover result
    crossover = mdl.population_crossover(parents)
    print("\nCrossover Result: \n", crossover)

    # NEW POPULATION
    # get the mutation result
    mutation = mdl.population_mutation(crossover)
    print("\nMutation Result: \n", mutation)

    fitness = mdl.fitness_route(route, population)
    # calculate the best fitness value by looking for the minimum value
    # or the smallest fitness value because
    # what we are looking for is the shortest route
    best_fitness = np.where(fitness == min(fitness))
    best_fitness = best_fitness[0][0]
    print("\nGeneration Distance: \n", fitness)

    # NEW POPULATION/GENERATION
    # create the shortest route generations graphic
    plt.title('Shortest Route Generation')
    plt.ylabel('Mutation')
    plt.xlabel('Fitness')
    plt.plot(mutation[best_fitness], fitness, marker='o', linewidth=4, markersize=12, linestyle='-', color='red')
    plt.show()
    print("\nGeneration Best Fitness: ", 1 / (fitness[best_fitness]))


parents = mdl.shortest_parents(population, fitness)
crossover = mdl.population_crossover(parents)
mutation = mdl.population_mutation(crossover)
fitness = mdl.fitness_route(route, population)
best_fitness = np.where(fitness == min(fitness))
best_fitness = best_fitness[0][0]

# FINAL POPULATION
# get the final population, the final distance, the best distance,
# the best fitness value, and the best chromosome
print("\nFinal Population: \n", mutation)
print("\nFinal Distance: \n", fitness)
print("\nBest Distance: ", fitness[best_fitness])
print("\nBest Fitness: ", 1 / (fitness[best_fitness]))
print("\nBest Chromosome: ", mutation[best_fitness])

# create the final shortest route graphic
plt.title('Final Shortest Route')
plt.ylabel('Mutation')
plt.xlabel('Fitness')
plt.plot(mutation[best_fitness], fitness, marker='o', linewidth=4, markersize=12, linestyle='-', color='red')
plt.show()
