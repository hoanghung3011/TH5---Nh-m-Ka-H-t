import numpy as np
INF=999
Broadcast=[[INF,85,175,200,20,100],
     [85,INF,125,175,100,160],
     [175,125,INF,100,200,250],
     [200,175,100,INF,210,220],
     [20,100,200,210,INF,100],
     [100,160,250,220,100,INF]]
vertexCount = len(Broadcast[0]) 
colorCount = 0 
level = [] 
colorName= []
for i in range(vertexCount):
    colorName.append(0)
for i in range(vertexCount):
    for j in range(vertexCount):
        if Broadcast[i][j] <= 150:
            Broadcast[i][j] = 1
        else: Broadcast[i][j] = 0
for i in range(vertexCount):
    level.append(np.sum(Broadcast[i]))
def vertexPick(level):
    levelMax = max(level)
    for i in range(vertexCount):
        if level[i] == levelMax:
            return i
def colorPick(S):
    global colorCount 
    while color < colorCount:
        OK = 1
        for i in range(vertexCount):
            if Broadcast[S][i] == 1 and colorName[i] == color:
                OK = 0
                break
        if OK == 1:
            return color
        color += 1
    color = colorCount
    colorCount += 1
    return color
print(Broadcast)
print(level)
print("Order of vertices to coloring:")
for k in range(vertexCount):
    S=vertexPick(level)
    print(S)
    color = colorPick(S)
    colorName[S] = color
    level[S] = -1
print("Number of channels to broadcast is: ",colorCount)
for i in range(vertexCount):
    print("Channel ",i," is broadcast in ",colorName[i])
