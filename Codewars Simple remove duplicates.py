def solve(arr): 
    reversed_arr = list(reversed(arr))

    answer = []

    for element in reversed_arr:
        if element not in answer:
            answer.append(element)
    
    answer.reverse()

    return answer





print(solve([3,4,4,3,6,3]))

