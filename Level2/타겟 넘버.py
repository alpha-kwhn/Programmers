numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    lis = []
    def BFS(index, answer):
        if index == len(numbers) - 1:
            lis.append(answer + numbers[index])
            lis.append(answer - numbers[index])
        else:
            BFS(index+1, answer + numbers[index])
            BFS(index+1, answer - numbers[index])
    BFS(0, 0)
    lis.sort()
    return lis.count(target)

did = solution(numbers, target)
print(did)
