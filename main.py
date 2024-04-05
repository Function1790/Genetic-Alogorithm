import numpy as np
from random import randint


def copyArr(arr):
    return [i for i in arr]


def sortArr(arr):
    for i in range(len(arr) - 1):
        least = i
        for j in range(i, len(arr)):
            if sum(arr[least]) > sum(arr[j]):
                least = j
        temp = copyArr(arr[i])
        arr[i] = copyArr(arr[least])
        arr[least] = temp
    return arr

def randState():
    return randint(0, 1)


def randChoice(a, b):
    return np.random.choice([a, b], replace=False)


def Crossover(arr1, arr2):
    return [randChoice(arr1[i], arr2[i]) for i in range(len(arr1))]


# 초기화
SELECT_COUNT = 10
GENE_COUNT = 40
FEATURE_COUNT = 100
chromosome = np.round(np.random.rand(GENE_COUNT, FEATURE_COUNT))


def evolve(chromosome):
    # 선택
    sorted_chromosome = np.flip(sortArr(chromosome))[0:SELECT_COUNT]
    # print("선택")
    # print(sorted_chromosome)

    # 교차
    crossovered = []
    _length = len(sorted_chromosome)
    for i in range(GENE_COUNT):
        a = sorted_chromosome[randint(0, _length - 1)]
        b = sorted_chromosome[randint(0, _length - 1)]
        crossovered.append(Crossover(a, b))
    crossovered = np.array(crossovered)
    # print("\n교차")
    # print(crossovered)

    # 변이
    return crossovered


def evaluate(result):
    temp = [sum(i) for i in chromosome]
    return sum(temp) / len(temp)


print(evaluate(chromosome))
for i in range(100):
    chromosome = evolve(chromosome)
    print(f"\n[ GENERATION-{i+1} ]")
    print(evaluate(chromosome))
