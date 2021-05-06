# https://www.acmicpc.net/problem/5555

# 첫 번째 줄에는 찾고자 하는 문자열을 입력합니다.
# 1자 이상 10자 이하의 대문자로 구성되어 있습니다.
find_string = input()

# 두 번째 줄에는 반지의 개수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 찾고자 하는 문자열이 있는 반지의 개수를 저장하는 변수를 선언합니다.
string_ring_count = 0

# 반지의 개수 N만큼 반복합니다.
for ring_index in range(N):
    # 이번 반지에 각인된 문자열을 입력합니다.
    ring = input()
    # 시작과 끝이 연결되어 있는 경우를 고려하기 위해
    # 입력한 문자열에 똑같은 문자열을 하나 더 연결해줍니다.
    ring += ring

    # 이번 반지에 찾고자 하는 문자열이 있는 경우
    if ring.find(find_string) != -1:
        # string_ring_count에 1을 더해줍니다.
        string_ring_count += 1

# 찾고자 하는 문자열이 있는 반지의 개수를 출력합니다.
print(string_ring_count)