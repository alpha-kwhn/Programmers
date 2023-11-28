def solution(elements):
    sets = set()
    lengths = 1

    while lengths <= len(elements) - lengths:
        container = []
        for i in range(len(elements)):
            if i + lengths <= len(elements):
                container.append(sum(elements[i:i + lengths]))
                container.append(sum(elements[i + lengths:] + elements[:i]))
            else:
                p = (i + lengths) - len(elements)
                tmp = elements[i:] + elements[:p]
                tmp2 = elements[p:i]
                container.append(sum(tmp))
                container.append(tmp2)
        sets = sets.union(set(container))
        lengths += 1
    sets.add(sum(elements))
    return len(sets)