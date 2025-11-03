def solution(babbling):
    answer = 0
    
    wordList = ["aya", "ye", "woo", "ma"]
    
    wordPos = -1
    
    for case in babbling:
        wordPos = -1
        while(len(case) > 0):
            change = False
            for word in wordList:
                if len(case) >= len(word) and word == case[:len(word)] and wordPos != wordList.index(word):
                    case = case[len(word):]
                    wordPos = wordList.index(word)
                    change = True
                    break
                
            if(not change):
                break
                
        if(len(case) == 0):
            answer += 1
            
    return answer