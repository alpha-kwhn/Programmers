col, row = map(int, input().split())

target = []

for i in range(row):
    lis = min(list(map(int, input().split())))
    target.append(lis)

target.sort()
print(target[-1])


