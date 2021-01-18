# https://www.acmicpc.net/problem/15726

# 첫째 줄에 세 개 정수 A, B, C 입력
# 1 <= A, B, C <= 1,000,000
# 답은 int 범위를 벗어나지 않는다.
A, B, C = map(int, input().split(' '))

# 곱셈, 나눗셈 순서의 결과를 저장하는 변수
multi_divi = int(A * B / C)
# 나눗셈, 곱셈 순서의 결과를 저장하는 변수
divi_multi = int(A / B * C)

# 위의 두 값 중 더 큰 값을 출력한다.
print(max(multi_divi, divi_multi))