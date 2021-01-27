# https://www.acmicpc.net/problem/14909

# 첫째 줄에 최대 1,000,000개의 정수를 입력합니다.
# 입력하는 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같습니다.
nums = list(map(int, input().split(' ')))

# 양의 정수의 개수를 저장하는 변수입니다.
positive = 0

# 리스트 변수에 저장된 숫자 하나마다 검사해봅니다.
for num in nums:
    # 현재의 수가 양수라면
    if num > 0:
        # 양수의 개수에 1을 더해줍니다.
        positive += 1

# 양수의 개수를 출력합니다.
print(positive)