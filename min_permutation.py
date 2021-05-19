def min_permutation(n):
    # Given a number, find the permutation with the 
    # smallest absolute value (no leading zeros).
    #-20 => -20
    #-32 => -23
    #0 => 0
    #10 => 10
    #29394 => 23499 

    newList = list(str(n))

    #Sort the list
    newList.sort()
    zeros = []

    # Get all the zeros
    for x in range(newList.count("0")):
        zeros.append("0")
    
    # Delete them all
    while "0" in newList:
        newList.remove("0")

    if len(newList) == 0:
        return 0

    # Put them right after the second digit if theres a -, else put them after the first digit 
    if len(newList) > 1 and newList[0] == "-":
        for element in zeros:
            newList.insert(2,element)
    else:
        for element in zeros:
            newList.insert(1,element)

    stringanswer = "".join(newList)
    return int(stringanswer)


print(min_permutation(2020568))
