def mirrorString(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + mirrorString(s[:-1])
    
print(mirrorString("chicken"))