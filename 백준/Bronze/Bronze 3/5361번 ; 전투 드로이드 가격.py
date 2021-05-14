# https://www.acmicpc.net/problem/5361

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 테스트 케이스의 개수를 입력합니다.
test_case_cnt = int(stdin.readline())

# 테스트 케이스의 개수만큼 반복합니다.
for test_case_idx in range(test_case_cnt):
    # 음이 아닌 정수 다섯 개 A, B, C, D, E를 입력합니다.
    # 정수형으로 변환해서 변수에 저장합니다.
    A, B, C, D, E = map(int, stdin.readline().split(' '))

    # 각 부품의 개수와 가격을 계산해서 비용의 총합을 저장하는 변수를 선언합니다.
    # 정답은 1억보다 작거나 같습니다.
    cost = A * 350.34 + B * 230.9 + C * 190.55 + D * 125.3 + E * 180.9

    # cost의 값을 출력 형식에 맞게 $와 함께 소수점 둘째 자리까지 출력합니다.
    print(f"${'{:.2f}'.format(cost)}")