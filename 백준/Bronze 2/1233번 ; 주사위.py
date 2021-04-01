# https://www.acmicpc.net/problem/1233

# S1, S2, S3 입력
# 2 <= S1 <= 20
# 2 <= S2 <= 20
# 2 <= S3 <= 20
S1, S2, S3 = map(int, input().split(' '))

# 각 합계와 빈도수를 연결한 dictionary
sum_frequency = {}

#
max_frequency_sum = 0
max_frequency = 0

# S1, S2, S3를 1부터 차례로 올려가면서 더해봅니다.
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            sum = i + j + k

            # 앞서서 똑같은 합이 나왔다면
            if sum in sum_frequency:
                # 그 합의 개수에 1 추가
                sum_frequency[sum] += 1
            # 합이 이번 차례에 처음 나왔다면
            else:
                # 1
                sum_frequency[sum] = 1

for key in sum_frequency:
    if sum_frequency[key] > max_frequency:
        max_frequency_sum = key
        max_frequency = sum_frequency[key]
    elif sum_frequency[key] == max_frequency:
        if max_frequency_sum > key:
            max_frequency_sum = key
    else:
        continue

print(max_frequency_sum)