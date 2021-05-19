# Codewars question to replace repeating letters to the next letter, so "aa" to "b"
def last_survivors(string):
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyza"
    newString = ''.join(sorted(string))
    for element in ascii_lowercase:
        if (element+element) in newString:
            recursionString = newString.replace((element+element),ascii_lowercase[ascii_lowercase.index(element)+1])
            return last_survivors(recursionString)
    else:
        return newString

print(last_survivors("aabaaaazz"))