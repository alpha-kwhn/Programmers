from itertools import permutations
import re

expression = "100-200*300-500+20"

def solution(expression):
    yeonsan = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '+', '*'], ['-', '*', '+']]
    #연산자 우선순위 조합 생성

    result = re.split('([0-9]+)', expression)
    result = result[1:-1]
    #숫자와 연산자를 문자열에서 분해하고 리스트를 생성함

    answer = []
    for t in yeonsan:
        tap = result
        stack = []
        for i in t:
            for j in tap:
                if len(stack) == 0:
                    stack.append(j)
                elif stack[-1] == i:
                    if i == '*':
                        compute = int(stack.pop(-2)) * int(j)
                        stack.pop()
                        stack.append(compute)
                    elif i == '+':
                        compute = int(stack.pop(-2)) + int(j)
                        stack.pop()
                        stack.append(compute)
                    elif i == '-':
                        compute = int(stack.pop(-2)) - int(j)
                        stack.pop()
                        stack.append(compute)
                    print(stack)
                else:
                    stack.append(j)
        answer.append(stack)
    return answer




did = solution(expression)
print(did)