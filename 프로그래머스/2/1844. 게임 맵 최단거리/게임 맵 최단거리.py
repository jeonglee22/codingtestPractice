def solution(maps):
    distances = [[10000 for j in range(len(maps[0]))] for i in range(len(maps))]
    posStack = list()
    
    posStack.append((len(maps) - 1, len(maps[0]) - 1))
    distances[len(maps) - 1][len(maps[0]) - 1] = 1
    
    while len(posStack) > 0:
        currentPos = posStack.pop(0)
        posX = currentPos[0]
        posY = currentPos[1]
        
        nextDistance = distances[posX][posY] + 1
    
        for i in range(4):
            newPosY = posY + (2 - i if (i % 2 == 1) else 0)
            newPosX = posX + (i - 1 if (i % 2 == 0) else 0)

            if (newPosX > len(maps) - 1 or newPosX < 0 or
                newPosY > len(maps[0]) - 1 or newPosY < 0 or
                maps[newPosX][newPosY] == 0 or distances[newPosX][newPosY] != 10000):
                continue
            
            if(newPosX == 0 and newPosY == 0):
                return nextDistance

            distances[newPosX][newPosY] = nextDistance
            posStack.append((newPosX, newPosY))
    
    return -1