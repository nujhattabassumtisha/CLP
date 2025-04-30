import random

def get_product(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def fitness(lst, target):
    return -abs(target - get_product(lst))

def mutate(lst):
    idx = random.randint(0, len(lst) - 1)
    lst[idx] = random.randint(1, 9)
    return lst

def crossover(a, b):
    point = random.randint(1, len(a) - 1)
    return a[:point] + b[point:]

def genetic_algorithm(T, k):
    population = [[random.randint(1, 9) for _ in range(k)] for _ in range(100)]

    for _ in range(1000):  
        population.sort(key=lambda x: fitness(x, T), reverse=True)

        if get_product(population[0]) == T:
            return population[0]

        new_pop = population[:10]  
        while len(new_pop) < 100:
            p1 = random.choice(population[:20])
            p2 = random.choice(population[:20])
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    return None

T = int(input("T: "))
k = int(input("k: "))

result = genetic_algorithm(T, k)

if result:
    print(*result)
