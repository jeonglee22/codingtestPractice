def solution(word):
    answer = 0
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(len(word)):
        index = alpha.index(word[i])
        
        for j in range(4 - i, -1, -1):
            answer += index * (5 ** j);
    
    answer += len(word)
    
    return answer