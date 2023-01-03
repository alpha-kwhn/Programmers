def solution(s):
    last_digit = len(s)-1
    values = [s[i] for i in range(last_digit, -1, -1)]
    stack = []
    print(values)

    for j in range(len(values)):
        x = values.pop()
        if x.isdigit():
            stack.append(int(x))
            if stack[-1] == 0 and stack[-2] == 1:
                stack.pop()
                stack.pop()
                stack.append(10)
        elif x.isalpha():
            if x == 'S':
                continue
            elif x == 'D':
                y = stack.pop()
                z = y**2
                stack.append(z)
            elif x == 'T':
                y = stack.pop()
                z = y**3
                stack.append(z)
        else:
            if x == '*':
                y = stack.pop()
                if len(stack) == 0:
                    stack.append(y*2)
                else:
                    z = stack.pop()
                    stack.append(z*2)
                    stack.append(y*2)
            elif x == '#':
                y = stack.pop()
                z = -1 * y
                stack.append(z)
        print(stack)
    return sum(stack)

print(solution("1S2D*3T*"))