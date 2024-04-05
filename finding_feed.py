import numpy as np
from os import system
from time import sleep

node_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
]

step=0
pos = np.array([1,1])
purpose = np.array([3,3])
direction = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
])

def displayMap():
    result=""
    for i in range(len(node_map)):
        for j in range(len(node_map[i])):
            if j==pos[0] and i==pos[1]:
                result+='▣'
            elif node_map[i][j]==0:
                result+='□'
            elif node_map[i][j]==1:
                result+='■'
        result+='\n'
    print(result)       

def move():
    global pos
    temp=np.array([distance(pos+i, purpose) for i in direction])
    weight=[-0.21388536, -1.59712725,  0.8754102 , -2.61252895]
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

score=0
while True:
    system('cls')
    step+=1
    if move():
        score=10+10/step
        break
    displayMap()
    sleep(.1)
    if pos[0]<0 or pos[0]>=len(node_map):
        score=10/distance(pos, purpose)+10/step
        break
    if pos[1]<0 or pos[1]>=len(node_map):
        score=10/distance(pos, purpose)+10/step
        break
print(score)