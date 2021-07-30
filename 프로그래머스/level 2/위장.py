# https://programmers.co.kr/learn/courses/30/lessons/42578

# 스파이가 가진 의상들이 담긴 2차원 리스트 clothes가 매개변수로 주어집니다.
def solution(clothes):
    # 서로 다른 옷의 조합의 수를 저장할 변수를 선언합니다.
    # 처음에는 1로 초기화합니다.
    cloth_comb_cnt = 1
    # 스파이가 가진 의상들을 의상의 종류로 구분해서 저장하기 위한 딕셔너리 변수를 선언합니다.
    clothes_class = {}

    # clothes에서 옷의 정보를 하나씩 반복해봅니다.
    for cloth in clothes:
        # 현재 옷의 정보에서 옷의 이름을 저장하는 변수를 선언합니다.
        cloth_name = cloth[0]
        # 현재 옷의 정보에서 옷의 종류를 저장하는 변수를 선언합니다.
        cloth_type = cloth[1]

        # 현재 옷의 종류가 한 번도 등장하지 않았던 종류라면
        if cloth_type not in clothes_class.keys():
            # 옷의 종류를 키로, 옷의 이름을 리스트 변수에 넣은 형태의 값으로 clothes_class에  저장합니다.
            clothes_class[cloth_type] = [cloth_name]
        # 현재 옷의 종류가 이전에 한 번 등장했던 종류라면
        elif cloth_type in clothes_class.keys():
            # clothes_class에서 종류에 해당하는 키를 찾고 그 값인 리스트에 현재 옷의 이름을 넣어줍니다.
            clothes_class[cloth_type].append(cloth_name)

    # 옷의 종류들이 담긴 리스트를 저장하는 변수를 선언합니다.
    cloth_types = clothes_class.keys()

    # 옷의 종류들에서 한 종류씩 반복해봅니다.
    for cloth_type in cloth_types:
        # 현재 옷의 종류에서 옷의 개수에 1을 더한 값을 저장하는 변수를 선언합니다.
        # 1을 더한 이유는 옷을 입지 않은 경우를 고려한 것입니다.
        type_length = len(clothes_class[cloth_type]) + 1
        # cloth_comb_cnt에 type_length를 곱해줍니다.
        cloth_comb_cnt *= type_length

    # 스파이는 최소 한 개의 의상은 입으므로 의상을 하나도 입지 않은 경우는 빼줘야합니다.
    # cloth_comb_cnt에 1을 뺀 값을 반환합니다.
    return cloth_comb_cnt - 1