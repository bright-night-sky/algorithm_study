# https://codeup.kr/problem.php?id=1222

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 현재 경기 타임, 1반 득점, 2반 득점을 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
cur_time, class1_score, class2_score = map(int, stdin.readline().split())
# 남은 경기시간을 저장하는 변수를 선언합니다.
remain_time = 90 - cur_time
# 투입된 성익이가 넣을 골의 개수를 저장할 변수를 선언합니다.
# 처음에는 0으로 초기화합니다.
sungik_goal = 0

# 성익이는 투입되자마자 한 골을 넣고 5분마다 한 골씩 넣으며,
# 딱 90분이 되면 성익이가 골을 넣는 시간이라고 해도 넣을 수 없습니다.

# 남은 시간이 5의 배수라면
if remain_time % 5 == 0:
    # 성익이가 넣을 골의 개수는 남은 시간을 5로 나눈 몫입니다.
    sungik_goal = remain_time // 5
# 남은 시간이 5의 배수가 아니라면
else:
    # 성익이가 넣을 골의 개수는 남은 시간을 5로 나눈 몫에 1을 더한 값입니다.
    sungik_goal = remain_time // 5 + 1

# 기존의 1반 득점에 성익이가 넣은 골의 개수를 더해줍니다.
class1_score += sungik_goal

# 1반 득점이 2반 득점보다 크다면
if class1_score > class2_score:
    # 문자열 'win'을 출력합니다.
    print('win')
# 1반 득점이 2반 득점과 같다면
elif class1_score == class2_score:
    # 문자열 'same'을 출력합니다.
    print('same')
# 그 외의 경우인 1반 득점이 2반 득점보다 작다면
else:
    # 문자열 'lose'를 출력합니다.
    print('lose')