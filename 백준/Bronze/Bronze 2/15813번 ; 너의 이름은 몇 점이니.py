# https://www.acmicpc.net/problem/15813

# 첫 번째 줄에 이름의 길이를 입력합니다.
# 길이는 100자 이하입니다.
name_length = int(input())

# 두 번째 줄에는 이름이 띄어쓰기 없이 대문자로 입력합니다.
name = input()

# 이름점수를 저장하는 변수를 선언합니다.
name_score = 0

# 이름에서 한 글자씩 반복해봅니다.
for alphabet in name:
    # 대문자 A~Z의 아스키 코드는 65~91이므로
    # A의 점수가 1로 만드려면 각 아스키 코드에서 64를 빼고 난 뒤에
    # 이름점수에 더하면 됩니다.
    name_score += ord(alphabet) - 64

# 최종적인 이름점수를 출력합니다.
print(name_score)