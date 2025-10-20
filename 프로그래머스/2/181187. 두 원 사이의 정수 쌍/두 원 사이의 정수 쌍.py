import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1,r2):
        y1 = int((r2 ** 2 - i ** 2) ** 0.5)
        
        if r1 ** 2 - i ** 2 < 0:
            y2 = -1
        else:
            y2 = math.ceil((r1 ** 2 - i ** 2) ** 0.5) - 1

        answer += y1 - y2

    answer += 1    
    answer *= 4
    
    return answer