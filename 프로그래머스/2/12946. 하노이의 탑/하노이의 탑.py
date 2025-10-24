def hanoi(start, end, n):
    if n == 1:
        return [[start, end]]
    
    poslist = [1,2,3]
    poslist.remove(start)
    poslist.remove(end)
    other = poslist[0]
    
    return hanoi(start, other, n - 1) + [[start, end]] + hanoi(other, end, n - 1)
    

def solution(n):
    answer = [[]]

    return hanoi(1,3,n)