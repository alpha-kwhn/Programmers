land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

#며칠 전에 풀었던 풀이는 BFS를 이용한 재귀를 통한 풀이였다
#정답률은 높았으나, 재귀를 할 수 있는 max 깊이를 초과하는 문제가 발생했기에 비효율적인 코드가 되었다
#앞서 풀었던 가장 큰 정사각형 구하기 문제를 통해 유용함을 느꼈던 Dynamic Programming 알고리즘을 통해
#복잡한 문제를 단순하게 풀어보았다
#땅을 건널 때마다 각 인덱스에서 가질 수 있는 max값을 계속 갱신해줌으로써 각 목적지에서 나올 수 있는 최대 값을 모두 구한 후
#그 중 가장 큰 수를 구해 return 해주었더니 정답률, 효율성 모두 우수한 코드가 나올 수 있었다.

def solution(land):
    target = land[0]
    for i in range(1, len(land)):
        tos = [0, 0, 0, 0]
        for j in range(4):
            lis = []
            for p in range(4):
                if j != p:
                    tmp = target[p] + land[i][j]
                    lis.append(tmp)
            tos[j] = max(lis)
        target = tos
    return max(target)

did = solution(land)
print(did)