# https://programmers.co.kr/learn/courses/30/lessons/86491

# 각 명함의 가로 길이, 세로 길이가 들어있는 2차원 리스트 sizes가 매개변수로 주어집니다.
def solution(sizes):
    # 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 저장할 변수를 선언합니다.
    answer = 0
    # 각 명함들의 사이즈를 [긴 길이, 짧은 길이] 형태로 저장할 리스트 변수를 선언합니다.
    long_width_sizes = []

    # sizes에서 각 명함들을 하나씩 반복해봅니다.
    for size in sizes:
        # 이번 명함의 기존 사이즈에서 가로보다 세로 길이가 더 길다면
        if size[0] < size[1]:
            # 명함의 사이즈를 저장하고 있는 리스트 내부에서 둘의 위치를 바꿔줍니다.
            size[0], size[1] = size[1], size[0]

        # 이번 명함의 사이즈인 리스트를 long_width_sizes에 넣어줍니다.
        long_width_sizes.append(size)

    # 각 명함들에서 가로 길이들을 저장하는 리스트 변수를 선언합니다.
    widths = [size[0] for size in long_width_sizes]
    # 각 명함들에서 세로 길이들을 저장하는 리스트 변수를 선언합니다.
    heights = [size[1] for size in long_width_sizes]
    # 각 명함들에서 가로 길이 중 최대 길이와 세로 길이 중 최대 길이를 곱해
    # 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 변수 answer에 저장합니다.
    answer = max(widths) * max(heights)

    # 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 저장하고 있는 answer의 값을 반환합니다.
    return answer