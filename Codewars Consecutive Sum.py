def consecutive_sum(num):
    num_range = list(range(1,num+1))
    yeet_list = []

    if num == 0:
        return 0
    
    for element in num_range:
        sum_num = element
        counter = 1

        if element <= (round(num/2)):
            while sum_num < num:
                sum_num = sum_num + (element + counter)
                counter += 1

            if sum_num == num:
                yeet_list.append(list(range(element,counter+1)))

    return len(yeet_list)+1

print(consecutive_sum(9700000))