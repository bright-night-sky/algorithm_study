# https://www.acmicpc.net/problem/2745

# 10진법을 넘어가는 진법에서 숫자로 표시할 수 없는 자리들을 dictionary로 저장
A_to_Z= {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35
}

# 수 N, B진법 입력
# 2 <= B <= 36
# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
N, B = input().split(' ')

# 결과를 저장할 변수
result = 0

# 입력받은 숫자의 자리수마다 돌려본다.
for idx in range(0, len(N)):
    # 현재 자릿수가 숫자형태가 아닌 알파벳이라면
    if N[idx].isalpha():
        # 진법에 맞게 계산하고 결과에 저장
        result += A_to_Z[N[idx]] * (int(B) ** (len(N) - (idx + 1)))
    # 현재 자릿수가 숫자형태라면
    else:
        # 진법에 맞게 계산하고 결과에 저장
        result += int(N[idx]) * (int(B) ** (len(N) - (idx + 1)))

# 결과를 출력한다.
print(result)