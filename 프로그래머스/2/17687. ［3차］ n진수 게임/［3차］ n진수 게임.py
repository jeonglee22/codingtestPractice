def gettransbase(num, n):
    result = ''
    
    if(num == 0): return "0"
    
    while num > 0:
        remain = num % n
        if remain > 9:
            remain = chr(ord('A') + remain - 10)
        result = str(remain) + result
        num = num // n
    
    return result

def solution(n, t, m, p):
    answer = ''
    
    num = 0
    playerPos = 1
    basestr = ''
    while(len(answer) < t):
        if len(basestr) == 0:
            basestr = gettransbase(num, n)
        
        s = basestr[0]
        if playerPos == p:
            answer += s
        
        playerPos += 1
        if(playerPos > m):
            playerPos = 1
        
        if len(basestr) == 1:
            num += 1
            basestr = ''
        else:
            basestr = basestr[1:]
    
    return answer