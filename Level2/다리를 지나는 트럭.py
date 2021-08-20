bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length #가상의 다리를 만듬
    count = 0

    while bridge:
        count += 1 #시간은 계속 흘러가고, 그럴때마다 왼쪽으로 한칸씩 땡겨주는 작업을 해준다
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return count

did = solution(bridge_length, weight, truck_weights)
print(did)