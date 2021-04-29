# https://www.acmicpc.net/problem/9237

# 첫째 줄에는 묘목의 수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

# 둘째 줄에는 각 나무가 자라는데 며칠이 걸리는지를 나타낸 ti들을 공백으로 구분해 입력합니다.
# 1 <= ti <= 1,000,000
# 정수형으로 바꾸고 리스트 변수에 넣어줍니다.
t = list(map(int, input().split(' ')))

# 자라는데 가장 오래 걸리는 묘목부터 심어야 되므로
# 나무들이 자라는 데 걸리는 일수를 기준으로 내림차순 정렬을 합니다.
t.sort(reverse=True)

# 제일 오래 걸리는 날짜를 저장하는 변수를 선언합니다.
max_growing_day = 0

# 나무들을 하나씩 반복해봅니다.
for index in range(len(t)):
    # 현재 나무가 자라는데 걸리는 일수를 저장하는 변수를 선언합니다.
    # 나무는 하루에 하나씩만 심을 수 있으므로
    # 현재 나무가 자라는데 걸리는 일수는
    # 입력받은 숫자 + (인덱스값 + 1)입니다.
    ti_growing_day = t[index] + (index + 1)

    # 현재 나무가 자라는데 걸리는 일수가 이전까지의 나무 중 제일 오래 걸리는 날짜보다 길다면
    if max_growing_day < ti_growing_day:
        # 제일 오래 걸리는 날짜에 현재 나무가 자라는데 걸리는 일수를 저장합니다.
        max_growing_day = ti_growing_day

# 이장님을 초대하는 날짜는 나무가 다 자라고 난 다음 날이므로
# 제일 오래 걸리는 날짜 + 1을 출력해줍니다.
print(max_growing_day + 1)