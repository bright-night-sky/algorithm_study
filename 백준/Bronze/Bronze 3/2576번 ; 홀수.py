# https://www.acmicpc.net/problem/2576

# 홀수만 저장될 리스트 변수입니다.
odd_nums = []

# 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수를 입력합니다.
for i in range(0, 7):
    # 자연수를 입력합니다.
    num = int(input())

    # 입력된 자연수가 홀수라면
    if num % 2 == 1:
        # odd_nums 리스트 변수에 넣어줍니다.
        odd_nums.append(num)

# 만약 홀수를 입력하지 않았다면
if len(odd_nums) == 0:
    # -1을 출력합니다.
    print(-1)
# 홀수를 하나라도 입력했다면
else:
    # odd_nums에 저장된 홀수들의 합을 출력합니다.
    print(sum(odd_nums))

    # odd_nums에 저장된 홀수들 중 최솟값을 출력합니다.
    print(min(odd_nums))