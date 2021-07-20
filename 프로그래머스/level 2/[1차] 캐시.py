# https://programmers.co.kr/learn/courses/30/lessons/17680

# 캐시 크기 cacheSize, 도시 이름 리스트 cities가 매개변수로 주어집니다.
def solution(cacheSize, cities):
    # 총 실행시간을 저장할 변수를 선언합니다.
    time = 0

    # cacheSize가 0인 경우
    if cacheSize == 0:
        # 총 실행시간은 cities의 길이에 cache miss인 경우의 실행시간 5를 곱한 값입니다.
        time = len(cities) * 5
    # cacheSize가 0이 아닌 경우
    else:
        # cities에 있는 모든 도시 이름들을 소문자로 처리해줍니다.
        cities = list(map(lambda city: city.lower(), cities))
        # cache를 하나 만들어줍니다.
        # 리스트 변수로 선언합니다.
        cache = []

        # cities에 있는 도시 하나마다 반복해봅니다.
        for city in cities:
            # 현재 도시가 cache에 들어있지 않다면
            if city not in cache:
                # cache에 현재 도시를 넣어줍니다.
                cache.append(city)
                # cache miss이므로 총 실행시간에 5를 더해줍니다.
                time += 5

                # 현재 도시를 넣고 난 뒤 cache의 길이가 cacheSize 보다 크다면
                if len(cache) > cacheSize:
                    # cache의 맨 앞에 있는 도시를 삭제해줍니다.
                    del cache[0]
            # 현재 도시가 cache에 들어있다면
            elif city in cache:
                # cache에 있는 현재 도시의 인덱스를 저장하는 변수를 선언합니다.
                city_idx = cache.index(city)
                # cache에 있는 현재 도시를 없애줍니다.
                cache.pop(city_idx)
                # 현재 도시를 cache의 끝에 다시 넣어줍니다.
                cache.append(city)
                # cache hit이므로 총 실행시간에 1을 더해줍니다.
                time += 1

    # 총 실행시간을 반환합니다.
    return time