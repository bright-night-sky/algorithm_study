# https://www.acmicpc.net/problem/2750

# 첫째 줄에 수의 개수 N 입력
# 1 <= N <= 1,000
N = int(input())

# 입력할 숫자들을 저장할 리스트 변수
nums = []

# 둘째 줄부터 N개의 줄에는 숫자 입력
for i in range(0, N):
    # 숫자 하나씩 입력
    num = int(input())
    # 입력한 숫자를 nums 리스트 변수에 삽입
    nums.append(num)

# nums 리스트 내부의 숫자들을 오름차순으로 정렬
nums = sorted(nums)

# 오름차순된 nums 리스트 내부의 숫자들을 한 줄씩 출력
for num in nums:
    print(num)