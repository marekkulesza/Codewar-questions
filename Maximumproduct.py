def adjacent_element_product(newList):

    flag = 0

    counter1 = 0
    counter2 = 1
    counter3 = 2

    if len(newList) == 2:
        return newList[counter1] * newList[counter2]

    a = newList[counter1] * newList[counter2]
    b = newList[counter2] * newList[counter3]

    while True:

        if a > b:
            a = a
            if (len(newList)-2) <= flag:
                if a > b:
                    return a
                else:
                    return b
            b = newList[counter2] * newList[counter3]
        else:
            a = newList[counter1] * newList[counter2]
            b = b
        
        counter1 += 1
        counter2 += 1
        counter3 += 1
        flag += 1
        
        if (len(newList)-1) <= flag:
            if a > b:
                return a
            else:
                return b

        

print(adjacent_element_product([1, 5, 10, 9]))