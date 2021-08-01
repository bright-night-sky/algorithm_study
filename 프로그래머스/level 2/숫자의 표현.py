# https://programmers.co.kr/learn/courses/30/lessons/12924

# 자연수 n이 매개변수로 주어집니다.
def solution(n):
    # 연속된 자연수들로 n을 표현하는 방법의 수를 저장할 변수를 선언합니다.
    answer = 0
    # 연속한 자연수들 중에서 시작하는 수를 1부터 어디까지 셀 것인지를 저장하는 변수를 선언합니다.
    # 예제의 n=15일 때, 시작하는 수는 1, 4, 7입니다.
    # 시작하는 수는 n의 절반까지 생각하면 됩니다.
    limit = n // 2 + 1

    # 시작하는 수를 1부터 limit까지 반복해봅니다.
    for start in range(1, limit):
        # 연속한 자연수들의 합을 저장할 변수를 선언합니다.
        # 시작하는 수인 start로 초기화합니다.
        continue_sum = start

        # 계속 반복해봅니다.
        while True:
            # 연속한 자연수들을 더해야하므로 start에 1을 더해 그 다음 숫자를 저장합니다.
            start += 1
            # continue_sum에 다음 숫자를 더해갑니다.
            continue_sum += start

            # continue_sum이 n보다 크다면
            if continue_sum > n:
                # 이번 케이스에서는 n을 연속한 자연수로 표현하지 못하므로 그냥 반복문을 탈출합니다.
                break
            # continue_sum이 n과 같다면
            elif continue_sum == n:
                # 이번 케이스에서는 n을 연속한 자연수로 표현할 수 있으므로 answer에 1을 더합니다.
                answer += 1
                # 반복문을 탈출합니다.
                break

    # 예제의 n=15일 때, 마지막 케이스인 15=15와 같이 그 수 자체도 연속한 자연수들로 표현하는 것이므로
    # answer에 1을 더하고 반환합니다.
    return answer + 1