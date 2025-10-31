def solution(n, wires):
    answer = -1
    
    for wire in wires:
        subconnect = [wire[0]]
        pos = 0
        
        wires2 = [i for i in wires]
        while len(subconnect) != pos:
            node = subconnect[pos]
            index = 0
            while index < len(wires2):
                other = wires2[index]
                if wire == other: 
                    index += 1
                    continue
                
                if node in other:
                    subconnect.append(other[1 - other.index(node)])
                    wires2.remove(other)
                else:
                    index += 1
            pos += 1
        
        currentDiffer = abs(n - len(subconnect) - len(subconnect))
        if (answer == -1 or currentDiffer < answer):
            answer = currentDiffer
    
    return answer