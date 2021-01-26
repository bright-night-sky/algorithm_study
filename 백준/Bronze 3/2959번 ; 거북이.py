# https://www.acmicpc.net/problem/2959

# 첫째 줄에 거북이가 생각한 네 양의 정수 A, B, C, D를 공백으로 구분해서 입력합니다.
# 0 < A, B, C, D < 100
# 입력받은 4개의 숫자들을 리스트 변수에 넣어줍니다.
A_to_D = list(map(int, input().split(' ')))

# 직사각형의 한쪽 길이는 두 번째로 큰 숫자이고,
# 다른 한쪽 길이는 가장 작은 숫자이다.
# 우선 A_to_D를 오름차순으로 정렬해줍니다.
A_to_D = sorted(A_to_D)

# 정렬된 A_to_D에서 두 번째로 큰 숫자를 한쪽 변의 변수로 저장해줍니다.
side_one = A_to_D[2]
# 정렬된 A_to_D에서 제일 작은 숫자를 다른 한쪽 변의 변수로 저장해줍니다.
side_two = A_to_D[0]

# 직사각형의 면적을 계산해줍니다.
area = side_one * side_two

# 결과를 출력합니다.
print(area)