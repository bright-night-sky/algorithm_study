# https://www.acmicpc.net/problem/21567

# A, B, C는 모두 1,000,000보다 작은 자연수입니다.
# 첫째 줄에 A를 입력합니다.
A = int(input())
# 둘째 줄에 B를 입력합니다.
B = int(input())
# 셋째 줄에 C를 입력합니다.
C = int(input())

# A, B, C를 곱한 결과를 문자열로 변환해서 저장한 변수를 선언합니다.
multiple = str(A * B * C)

# 0에서 9까지 반복해봅니다.
for num in range(10):
    # multiple의 값에서 현재 숫자의 개수를 세어 출력합니다.
    print(multiple.count(str(num)))