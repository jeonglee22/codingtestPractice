def maxSum(sumlist, i, j, triangle):
    if i == len(triangle) - 1:
        return triangle[i][j]
    
    if sumlist[i][j] != 0:
        return sumlist[i][j]
    
    rightSum = maxSum(sumlist, i+1, j+1, triangle)
    downSum = maxSum(sumlist, i+1, j, triangle)
    
    if rightSum >= downSum:
        sumlist[i][j] = rightSum + triangle[i][j]
    else:
        sumlist[i][j] = downSum + triangle[i][j]
        
    return sumlist[i][j]

def solution(triangle):
    answer = 0
    
    sumlist = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
    result = maxSum(sumlist, 0,0, triangle)
    
    return result