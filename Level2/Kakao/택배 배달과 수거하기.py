# n개의 집에 택배배달, 배달 다니면서 빈 재활용 택배상자 수집
# i번째 집은 창고에서 i 만큼 떨어져 있음
# 트럭에는 최대 cap개의 상자 실을 수 있음
# 각 집마다 배달할 재활용 택배 상자의 개수, 수거할 빈 재활용 택배 상자 개수 주어짐
# 트럭 하나로 모든 배달, 수거 마치고 창고 올 수 있는 최소 이동 거리 구하기
def solution(cap, n, deliveries, pickups):
    distance = 0

    while deliveries[-1] == 0:
        deliveries.pop()
        if len(deliveries) == 0:
            break
    while pickups[-1] == 0 and pickups:
        pickups.pop()
        if len(pickups) == 0:
            break

    while deliveries or pickups:
        distance += (max(len(deliveries), len(pickups)) * 2)
        count_deliver = 0
        count_pickup = 0

        while deliveries:
            if count_deliver + deliveries[-1] <= cap:
                count_deliver += deliveries.pop()
            else:
                deliveries[-1] -= (cap - count_deliver)
                break

        while pickups:
            if count_pickup + pickups[-1] <= cap:
                count_pickup += pickups.pop()
            else:
                pickups[-1] -= (cap - count_pickup)
                break

    return distance