def solution(arr):
    answer = [0,0]

    if len(arr) == 1:
        answer[arr[0][0]] += 1
        return answer
    if len(arr) == 2:
        if (arr[0][0] == arr[0][1] and arr[0][1] == arr[1][0] and arr[1][0] == arr[1][1]):
            answer[arr[0][0]] += 1
        else:
            answer[arr[0][0]] += 1
            answer[arr[0][1]] += 1
            answer[arr[1][0]] += 1
            answer[arr[1][1]] += 1
        return answer
    
    leftUp = [i[0 : len(arr) // 2] for i in arr[0 : len(arr) //2]]
    leftDown = [i[0 : len(arr) // 2] for i in arr[len(arr) // 2 : len(arr)]]
    rightUp = [i[len(arr) // 2 : len(arr)] for i in arr[0 : len(arr) // 2]]
    rightDown = [i[len(arr) // 2 : len(arr)] for i in arr[len(arr) // 2 : len(arr)]]
    
    leftUpSol = solution(leftUp)
    leftDownSol = solution(leftDown)
    rightUpSol = solution(rightUp)
    rightDownSol = solution(rightDown)
    
    if(not(leftUpSol == leftDownSol and leftDownSol == rightUpSol and rightUpSol == rightDownSol and
            sum(leftUpSol) == 1)):
        answer[0] = leftUpSol[0] + leftDownSol[0] + rightUpSol[0] + rightDownSol[0]
        answer[1] = leftUpSol[1] + leftDownSol[1] + rightUpSol[1] + rightDownSol[1]
    else:
        answer[0] = leftUpSol[0]
        answer[1] = leftUpSol[1]
    
    return answer