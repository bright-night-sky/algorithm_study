# https://www.acmicpc.net/problem/4435

# 첫째 줄에 전투의 개수 T를 입력합니다.
# 음이 아닌 정수입니다.
T = int(input())

# 전투의 개수 T만큼 반복해봅니다.
for battle_num in range(T):
    # 각 전투의 첫째 줄에는 간달프 군대에 참여한 종족의 수를 공백으로 구분해 입력합니다.
    # 호빗, 인간, 엘프, 드워프, 독수리, 마법사 순입니다.
    # 리스트 변수로 만들어줍니다.
    gandalf_army = list(map(int, input().split(' ')))
    # 각 전투의 둘째 줄에는 사우론 군대에 참여한 종족의 수를 공백으로 구분해 입력합니다.
    # 오크, 인간, 워그, 고블린, 우럭하이, 트롤, 마법사 순입니다.
    # 리스트 변수로 만들어줍니다.
    sauron_army = list(map(int, input().split(' ')))

    # 각 군대의 점수의 합은 32비트 정수 제한을 넘지 않습니다.
    # 간달프의 군대의 각 종족의 점수에 맞게 계산해 저장한 변수를 선언합니다.
    # 한 줄로 선언하면 너무 길어서 보기 힘드므로 중간중간에 밑줄로 내려줍니다.
    gandalf_army_score = gandalf_army[0] + \
                         gandalf_army[1] * 2 + \
                         (gandalf_army[2] + gandalf_army[3]) * 3 + \
                         gandalf_army[4] * 4 + \
                         gandalf_army[5] * 10
    # 사우론의 군대의 각 종족의 점수에 맞게 계산해 저장한 변수를 선언합니다.
    # 한 줄로 선언하면 너무 길어서 보기 힘드므로 중간중간에 밑줄로 내려줍니다.
    sauron_army_score = sauron_army[0] + \
                        (sauron_army[1] + sauron_army[2] + sauron_army[3]) * 2 + \
                        sauron_army[4] * 3 + \
                        sauron_army[5] * 5 + \
                        sauron_army[6] * 10

    # 간달프의 군대의 점수가 사우론의 군대의 점수보다 크다면
    if gandalf_army_score > sauron_army_score:
        # Battle, 전투 번호, Good triumphs over Evil을 출력합니다.
        print(f"Battle {battle_num+1}: Good triumphs over Evil")
        # 간달프의 군대의 점수가 사우론의 군대의 점수보다 작다면
    elif gandalf_army_score < sauron_army_score:
        # Battle, 전투 번호, Evil eradicates all trace of Good을 출력합니다.
        print(f"Battle {battle_num+1}: Evil eradicates all trace of Good")
    # 간달프의 군대의 점수와 사우론의 군대의 점수보다 같다면
    else:
        # Battle, 전투 번호, No victor on this battle field을 출력합니다.
        print(f"Battle {battle_num+1}: No victor on this battle field")