# https://www.acmicpc.net/problem/9366

# readline을 사용하기 위해 import를 합니다.
from sys import stdin

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
# 1 <= T <= 100
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 삼각형의 각 변의 길이를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환합니다.
    # 1 <= A, B, C <= 1,000,000
    A, B, C = map(int, stdin.readline().split(' '))
    # 세 변 중 가장 긴 변의 길이를 저장하는 변수를 선언합니다.
    max_side = max(A, B, C)
    # 삼각형이 어떤 삼각형인지 저장할 변수를 선언합니다.
    triangle = None

    # 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 크거나 같다면
    if max_side >= A + B + C - max_side:
        # 삼각형이 될 수 없으므로 triangle 변수에 invalid!를 저장합니다.
        triangle = "invalid!"
    # 세 변의 길이가 모두 같다면
    elif A == B == C:
        # 정삼각형이므로 triangle 변수에 equilateral을 저장합니다.
        triangle = "equilateral"
    # 세 변의 길이가 모두 다르다면
    elif A != B != C:
        # 부등변삼각형이므로 triangle 변수에 scalene을 저장합니다.
        triangle = "scalene"
    # 나머지 경우는 두 개의 변의 길이가 같은 경우이므로
    else:
        # triangle 변수에 이등변삼각형인 isosceles를 저장합니다.
        triangle = "isosceles"

    # 출력 형식에 맞게 출력합니다.
    print(f"Case #{test_case_idx + 1}: {triangle}")