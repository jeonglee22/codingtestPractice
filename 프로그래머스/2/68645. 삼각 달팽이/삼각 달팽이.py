def solution(n):
    answer = []
    
    if n == 1:
        return [1]
    
    numlist = [[0 for i in range(n)] for j in range(n) ]
    numlist[0][0] = num = 1
    pos = [0,0]
    direction = [[1,0], [0,1], [-1,-1]]
    dirIndex = 0
    
    while(True):             
        checkNext = [pos[0], pos[1]]
        checkNext[0] += direction[dirIndex][0]
        checkNext[1] += direction[dirIndex][1]
        
        if(dirIndex == 0 and (checkNext[0] == n or numlist[checkNext[0]][checkNext[1]] != 0 )):
            dirIndex = 1
        elif(dirIndex == 1 and (checkNext[1] > checkNext[0] or numlist[checkNext[0]][checkNext[1]] != 0 )):
            dirIndex = 2
        elif(dirIndex == 2 and numlist[checkNext[0]][checkNext[1]] != 0):
            dirIndex = 0
        
        pos[0] += direction[dirIndex][0]
        pos[1] += direction[dirIndex][1]
        
        if(numlist[pos[0]][pos[1]] != 0):
            break
        
        num += 1
        numlist[pos[0]][pos[1]] = num
        
    for i in numlist:
        for j in i:
            if j != 0:
                answer.append(j)
    
    return answer