# https://codeup.kr/problem.php?id=1226

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 로또 당첨 번호 6개와 보너스 번호 1개를 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
# 총 번호 7개를 리스트에 넣어줍니다.
lotto_nums = stdin.readline().rstrip().split()
# 지혜가 가지고 있는 로또 번호 6개를 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
# 번호 6개를 리스트에 넣어줍니다.
jihye_nums = stdin.readline().rstrip().split()
# 로또 당첨 번호 6개를 따로 리스트 변수로 만들어줍니다.
winning_nums = lotto_nums[:6]
# 보너스 번호를 저장하는 변수를 선언합니다.
bonus_num = lotto_nums[-1]
# 지혜가 가지고 있는 로또 번호 중 당첨 번호와 일치하는 번호의 개수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
winning_num_cnt = 0
# 지혜가 가지고 있는 로또 번호 중 보너스 번호가 있는지 여부를 저장할 변수를 선언합니다.
# 처음에는 보너스 번호가 업다는 뜻인 False로 초기화합니다.
bonused = False

# 지혜가 가지고 있는 로또 번호를 하나씩 반복해봅니다.
for jihye_num in jihye_nums:
    # 현재 지혜의 로또 번호가 로또 당첨 번호에 속한다면
    if jihye_num in winning_nums:
        # 당첨 번호의 개수에 1을 더해줍니다.
        winning_num_cnt += 1

# 보너스 번호가 지혜가 가지고 있는 번호 중에 있다면
if bonus_num in jihye_nums:
    # bonused 변수의 값을 보너스 번호가 있다는 뜻인 True로 변경하빈다.
    bonused = True

# 지혜의 로또 번호들이 당첨 번호와 6개 모두 일치한다면
if winning_num_cnt == 6:
    # 1등을 의미하는 1을 출력합니다.
    print(1)
# 지혜의 로또 번호들이 당첨 번호와 5개와 일치하고 보너스 번호를 맞췄다면
elif winning_num_cnt == 5 and bonused:
    # 2등을 의미하는 2를 출력합니다.
    print(2)
# 지혜의 로또 번호들이 당첨 번호와 5개와 일치한다면
elif winning_num_cnt == 5:
    # 3등을 의미하는 3을 출력합니다.
    print(3)
# 지혜의 로또 번호들이 당첨 번호와 4개와 일치한다면
elif winning_num_cnt == 4:
    # 4등을 의미하는 4를 출력합니다.
    print(4)
# 지혜의 로또 번호들이 당첨 번호와 3개와 일치한다면
elif winning_num_cnt == 3:
    # 5등을 의미하는 5를 출력합니다.
    print(5)
# 그 외의 경우인 지혜의 로또 번호들이 당첨 번호와 2개 이하로 일치한다면
else:
    # 꽝을 의미하는 0을 출력합니다.
    print(0)