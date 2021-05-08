# https://www.acmicpc.net/problem/14910

# 첫째 줄에 공백으로 구분된 N개의 정수를 입력합니다.
# 1 <= N <= 1,000,000
# 각 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수입니다.
# 각 정수는 정수형으로 변환하고 리스트 변수에 넣어줍니다.
nums = list(map(int, input().split(' ')))

# nums에 있는 숫자들을 문제의 비내림차순인 오름차순으로 정렬한 리스트 변수를 따로 만들어줍니다.
sorted_nums = sorted(nums)

# nums와 sorted_nums가 같다면
if nums == sorted_nums:
    # 비내림차순이므로 Good을 출력합니다.
    print("Good")
# nums와 sorted_nums가 다르다면
else:
    # 비내림차순이 아니므로 Bad를 출력합니다.
    print("Bad")