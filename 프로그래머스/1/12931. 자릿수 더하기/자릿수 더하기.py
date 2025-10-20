def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while (n > 0):
        answer += n % 10
        n = n // 10

    return answer
