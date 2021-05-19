# Organizes a list either backwards or forwards 
# using R or L, then the list

def flip(side, lst):
    if side == "R":
        lst.sort()
        print(lst)
        
    if side == "L":
        lst.sort(reverse=True)
        print(lst)
    
    return lst
        

flip('R', [3, 2, 1, 2])
