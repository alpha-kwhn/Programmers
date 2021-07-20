absolutes = [5, 8, 9]
signs = [True, False, False]

def solution(absolutes, signs):
    size_a = len(absolutes)
    sum = 0

    for i in range (size_a):
        if signs[i] == False:
            sum += absolutes[i] * -1
        else:
            sum += absolutes[i]

    answer = sum
    return answer

bc = solution(absolutes, signs)
print(bc)
