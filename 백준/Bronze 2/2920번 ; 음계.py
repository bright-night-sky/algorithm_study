# https://www.acmicpc.net/problem/2920

# 첫째 줄에 8개의 숫자를 입력합니다.
notes = input()

# 1부터 8까지 차례대로 연주한 상태를 저장하는 변수를 선언합니다.
ascending_notes = "1 2 3 4 5 6 7 8"
# 8부터 1까지 차례대로 연주한 상태를 저장하는 변수를 선언합니다.
descending_notes = "8 7 6 5 4 3 2 1"

# 입력한 notes가 1부터 8까지 연주한 값이라면
if notes == ascending_notes:
    # ascending을 출력합니다.
    print("ascending")
# 입력한 notes가 8부터 1까지 연주한 값이라면
elif notes == descending_notes:
    # descending을 출력합니다.
    print("descending")
# 그 외의 연주라면
else:
    # mixed를 출력합니다.
    print("mixed")