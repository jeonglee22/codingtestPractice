def solution(dirs):
    answer = 0
    
    moveList = []
    currPos = [0,0]
    
    dirDict = { "U" : [-1,0], "D" : [1,0], "R" : [0,-1], "L" : [0,1]}
    
    for i in dirs:
        nextPos = [currPos[0] + dirDict[i][0], currPos[1] + dirDict[i][1]]
        if (nextPos[0] < -5 or nextPos[0] > 5 or nextPos[1] < -5 or nextPos[1] > 5):
            continue
        
        moveCase1 = [currPos, nextPos]
        moveCase2 = [nextPos, currPos]
        
        if moveCase1 in moveList or moveCase2 in moveList:
            currPos = nextPos
            continue
        
        moveList.append(moveCase1)
        currPos = nextPos
    
    return len(moveList)