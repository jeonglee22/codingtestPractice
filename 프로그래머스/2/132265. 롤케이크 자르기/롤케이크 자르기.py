def solution(topping):
    answer = 0
    
    leftDict = dict()
    rightDict = dict()
    
    for i in topping:
        if i in leftDict.keys():
            leftDict[i] += 1
        else:
            leftDict[i] = 1
    
    for i in topping:
        
        leftDict[i] -= 1
        if leftDict[i] == 0:
            leftDict.pop(i)
            
        if i in rightDict.keys():
            rightDict[i] += 1
        else:
            rightDict[i] = 1
            
        if (len(leftDict.keys()) == len(rightDict.keys())):
            answer+=1
    
    return answer