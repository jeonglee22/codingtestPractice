def solution(numbers, target):
    answer = 0

    if len(numbers) == 1:
        return int(numbers[0] - target == 0) + int(numbers[0] + target == 0)

    answer += (solution(numbers[1:], target - numbers[0]) +
                solution(numbers[1:], target + numbers[0]))
    
    return answer