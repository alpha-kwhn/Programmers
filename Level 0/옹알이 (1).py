def solution(babbling):
    able = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for item in babbling:
        target = item
        blank_num = 0
        for word in able:
            if word in target:
                target = target.replace(word, " ")   
                blank_num += 1
                if target == " " * blank_num:  
                    count += 1
                    break
    return count
