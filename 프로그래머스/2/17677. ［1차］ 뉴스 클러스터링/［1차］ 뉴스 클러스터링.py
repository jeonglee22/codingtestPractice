def solution(str1, str2):
    answer = 0
    
    sepStr1 = [str1[i:i+2].lower() for i in range(len(str1) - 1)]
    sepStr2 = [str2[i:i+2].lower() for i in range(len(str2) - 1)]

    pos = 0
    while (pos < len(sepStr1)):
        if not(sepStr1[pos][0] >= 'a' and sepStr1[pos][0] <= 'z'):
            sepStr1.remove(sepStr1[pos])
        elif not(sepStr1[pos][1] >= 'a' and sepStr1[pos][1] <= 'z'):
            sepStr1.remove(sepStr1[pos])
        else:
            pos+= 1
        
    pos = 0
    while (pos < len(sepStr2)):
        if not(sepStr2[pos][0] >= 'a' and sepStr2[pos][0] <= 'z'):
            sepStr2.remove(sepStr2[pos])
        elif not(sepStr2[pos][1] >= 'a' and sepStr2[pos][1] <= 'z'):
            sepStr2.remove(sepStr2[pos])
        else:
            pos+= 1
            
    total = len(sepStr1) + len(sepStr2)
    
    if total == 0: return 65536
    
    print(sepStr1)
    print(sepStr2)
    print(total)
    
    both = 0
    pos = 0
    while(pos < len(sepStr1)):
        if sepStr1[pos] in sepStr2:
            ele = sepStr1[pos]
            sepStr1.remove(ele)
            sepStr2.remove(ele)
            both += 1
        else:
            pos += 1
    
    total -= both
    
    answer = int((both / total) * 65536)
    
    return answer