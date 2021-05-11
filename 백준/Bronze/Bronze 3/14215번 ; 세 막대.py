# https://www.acmicpc.net/problem/14215

# 첫째 줄에 a, b, c를 입력합니다.
# 1 <= a, b, c <= 100
# 입력한 길이들을 리스트 변수에 넣어줍니다.
sides = list(map(int, input().split(' ')))

# 선들의 길이에 따라 오름차순으로 정렬해둡니다.
sort_sides = sorted(sides)

# a, b, c 중 가장 긴 변을 찾습니다.
longest = sort_sides[2]

# 나머지 두 변의 길이를 합치는 변수입니다.
rest_sum = sort_sides[0] + sort_sides[1]

# 세 변의 길이를 알 때 삼각형의 결정 조건은
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.

# 만약 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 길거나 같다면
if longest >= rest_sum:
    # 가장 긴 변의 길이를 다른 두 변의 길이의 합보다
    # 1만 작게 조절하면 삼각형의 둘레를 최대로 할 수 있습니다.
    sort_sides[2] = rest_sum - 1

# 세 변의 길이의 합을 출력합니다.
print(sort_sides[2] + rest_sum)