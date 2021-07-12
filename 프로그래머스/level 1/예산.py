# https://programmers.co.kr/learn/courses/30/lessons/12982

# 부서별로 신청한 금액이 들어있는 리스트 d, 총 예산인 budget이 매개변수로 주어집니다.
# d의 길이는 1 이상 100 이하이며, 각 원소는 1 이상 100,000 이하의 자연수입니다.
# budget은 1 이상 10,000,000 이하의 자연수입니다.
def solution(d, budget):
    # 최대로 지원할 수 있는 부서의 개수를 저장할 변수를 선언합니다.
    answer = 0
    # 부서별로 신청한 금액인 d의 값들을 오름차순으로 정렬합니다.
    d = sorted(d)
    # d의 길이를 저장하는 변수를 선언합니다.
    d_len = len(d)

    # 1부터 d의 길이만큼 반복해봅니다.
    for idx in range(1, d_len + 1):
        # 첫 번째 부서부터 현재 인덱스의 이전까지의 부서가 신청한 금액의 합계를 저장하는 변수를 선언합니다.
        department_sum = sum(d[:idx])

        # department_sum이 budget보다 작거나 같다면
        if department_sum <= budget:
            # answer에 현재 idx의 값을 저장합니다.
            answer = idx
        # department_sum이 budget보다 크다면
        else:
            # 반복문을 탈출합니다.
            break

    # 최대로 지원할 수 있는 부서의 개수를 저장한 answer의 값을 반환합니다.
    return answer