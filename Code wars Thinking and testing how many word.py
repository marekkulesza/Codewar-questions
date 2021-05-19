def testit(s):
    
    counterw = 0
    countero = 0
    counterr = 0
    counterd = 0
    for elements in s:
        if elements == "w" and "o" and "r" and "d":
            counterw += 1


    if (min(counterd,countero,counterr,counterw)) == 0:
        return 0
    else:
        print(min(counterd,countero,counterr,counterw))

s = ("I love codewars.")

testit(s)

###        if elements == "W":
###           counterw += 1
###        if elements == "o":
 ###           countero += 1
 ###       if elements == "O":
 ###           countero += 1
 ###       if elements == "r":
 ###           counterr += 1
 ###       if elements == "R":
 ###           counterr += 1
 ###       if elements == "d":
 ###           counterd += 1
 ###       if elements == "D":
 ###           counterd += 1
        