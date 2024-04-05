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
GENE_COUNT = 100
FEATURE_COUNT = 4
chromosome = np.random.rand(GENE_COUNT, FEATURE_COUNT)*10-5


def evolve(chromosome, evaluate):
    # 선택
    # 교차
    crossovered = []
    _length = len(chromosome)
    for i in range(GENE_COUNT):
        a = chromosome[randint(0, _length - 1)]
        b = chromosome[randint(0, _length - 1)]
        crossovered.append(Crossover(a, b))
    crossovered = np.array(crossovered)
    # print("\n교차")
    # print(crossovered)

    # 변이
    return crossovered


def evaluate(result):
    temp = [sum(i) for i in chromosome]
    return sum(temp) / len(temp)


#print(evaluate(chromosome))
#for i in range(100):
#    chromosome = evolve(chromosome)
#    print(f"\n[ GENERATION-{i+1} ]")
#    print(evaluate(chromosome))


node_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
]
# [1 2 3 4] 위 아래 우 좌
# [2 2 4 4]
#---------------
# [2 4 12 16]

step=0
pos = np.array([1,1])
purpose = np.array([3,3])
direction = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
])

def move(weight):
    global pos
    temp=np.array([distance(pos+i, purpose) for i in direction])
    calced = temp*weight
    index=-1
    for i in range(len(calced)):
        if calced[i]==max(calced):
            index=i
    if pos[0]==purpose[0] and pos[1]==purpose[1]:
        return True
    pos+=direction[index]
    return False


def distance(a, b):
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def run(chromosome):
    global step, pos
    scores=[]
    for i in range(len(chromosome)):
        weight=chromosome[i]
        pos=np.array([1,1])
        score=0
        while True:
            step+=1
            if move(weight):
                score=10-10/step
                break
            if pos[0]<0 or pos[0]>=len(node_map):
                score=10-10/step-distance(pos, purpose)
                break
            if pos[1]<0 or pos[1]>=len(node_map):
                score=10-10/step-distance(pos, purpose)
                break
            if step>100:
                score=-50
                break
        scores.append(score)
    return scores

for i in range(200):
    print(f"[ {i+1}세대 ]")
    scores=run(chromosome)
    sorted_scores=[i for i in scores]
    sorted_scores.sort()
    sorted_scores.reverse()
    sorted_data=[]
    for i in list(sorted_scores):
        for j in range(len(scores)):
            if i==scores[j]:
                sorted_data.append([chromosome[j], scores[j]])
    a=[i[0] for i in sorted_data]
    b=[i[1] for i in sorted_data]
    chromosome=evolve(a, b)
print(chromosome)