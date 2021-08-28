# https://codeup.kr/problem.php?id=1207

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 윷 4개의 상태를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환하고, 리스트 변수에 넣어줍니다.
yuts = list(map(int, stdin.readline().split()))
# 리스트 yuts에서 뒤집어진 상태의 윷인 1의 개수를 저장하는 변수를 선언합니다.
turned_yuts_cnt = yuts.count(1)

# 뒤집어진 윷의 개수가 1개라면, 즉, 1의 개수가 1개라면
if turned_yuts_cnt == 1:
    # 문자 '도'를 출력합니다.
    print('도')
# 뒤집어진 윷의 개수가 2개라면, 즉, 1의 개수가 2개라면
elif turned_yuts_cnt == 2:
    # 문자 '개'를 출력합니다.
    print('개')
# 뒤집어진 윷의 개수가 3개라면, 즉, 1의 개수가 3개라면
elif turned_yuts_cnt == 3:
    # 문자 '걸'을 출력합니다.
    print('걸')
# 뒤집어진 윷의 개수가 4개라면, 즉, 1의 개수가 4개라면
elif turned_yuts_cnt == 4:
    # 문자 '윷'을 출력합니다.
    print('윷')
# 그 외의 경우인 뒤집어진 윷이 없다면, 즉, 1의 개수가 0개라면
else:
    # 문자 '모'를 출력합니다.
    print('모')