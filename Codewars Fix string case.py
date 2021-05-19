def solve(s):
    
    if s.isupper():
        return s.upper()
    if s.islower():
        return s.lower()

    upper_letters = 0

    for element in s:
        if element.isupper():
            upper_letters += 1
        
    if upper_letters > round(len(s)/2):
        return s.upper()

    return s.lower()

print(solve(s))