def checkPrime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    
    primeList = [False] * 3000

    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                case = nums[i] + nums[j] + nums[k]

                if primeList[case - 1]:
                    answer += 1
                    continue
                
                if checkPrime(case):
                    primeList[case - 1] = True
                    answer += 1

    return answer