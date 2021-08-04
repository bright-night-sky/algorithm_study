# https://programmers.co.kr/learn/courses/30/lessons/42583


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

time = 1
bridge = []

while True:
    if truck_weights == []:
        print(time)
        break

    bridge_truck_sum = sum(map(lambda truck: truck[0], bridge))

    if bridge_truck_sum + truck_weights[0] <= weight:
        added_truck = truck_weights.pop(0)
        bridge.append([added_truck, 0])

    for truck in bridge:
        truck[1] += 1

        if truck[1] > bridge_length:
            bridge.pop(0)

    time += 1