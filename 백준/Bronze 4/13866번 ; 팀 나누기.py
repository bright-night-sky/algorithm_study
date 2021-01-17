# https://www.acmicpc.net/problem/13866

# 네 개의 정수 A, B, C, D 입력
# 0 <= A <= B <= C <= D <= 10^4
# 각 스킬 레벨을 차례대로 리스트에 삽입
skill_levels = list(map(int, input().split(' ')))

# skill_levels를 오름차순으로 정렬해준다.
skill_levels = sorted(skill_levels)

# 정렬된 skill_levels의 요소에서 맨 처음에 있는 값과 맨 끝에 있는 값을 더한 값과
# 중간의 두 값을 더한 값의 차이가 두 팀의 스킬 레벨 차이의 최솟값이다.
# 차이를 구해야하므로 절댓값 처리를 해준다.
print(abs((skill_levels[0] + skill_levels[3]) - (skill_levels[1] + skill_levels[2])))
