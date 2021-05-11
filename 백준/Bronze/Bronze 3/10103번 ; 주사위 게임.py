# https://www.acmicpc.net/problem/10103

# 첫째 줄에 라운드의 수 n을 입력합니다.
# 1 <= n <= 15
n = int(input())

# 창영이와 상덕이의 점수를 저장하는 변수입니다.
# 초기 점수는 100점입니다.
changyoung = 100
sangduk = 100

# 라운드의 수만큼 돌려봅니다.
for i in range(0, n):
    # 첫 번째 정수인 창영이의 주사위 숫자, 두 번째 정수인 상덕이의 주사위 숫자를 입력합니다.
    # 두 정수는 항상 1보다 크거나 같고, 6보다 작거나 같습니다.
    changyoung_dice, sangduk_dice = map(int, input().split(' '))

    # 창영이와 상덕이의 주사위를 비교해봅니다.
    # 만약, 창영이 주사위의 숫자가 더 크다면
    if changyoung_dice > sangduk_dice:
        # 상덕이의 점수에서 창영이 주사위 숫자만큼 뺍니다.
        sangduk -= changyoung_dice
    # 만약, 상덕이 주사위의 숫자가 더 크다면
    elif changyoung_dice < sangduk_dice:
        # 창영이의 점수에서 상덕이 주사위 숫자만큼 뺍니다.
        changyoung -= sangduk_dice
    # 두 사람의 주사위 숫자가 같다면,
    else:
        # 아무도 점수를 잃지 않습니다.
        continue

# 모든 라운드가 끝나면 창영이의 점수를 먼저 출력합니다.
print(changyoung)
# 그 다음 줄에 상덕이의 점수를 출력합니다.
print(sangduk)