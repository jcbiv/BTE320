s1 = 'abcdefg'
s2 = 'abdght'

for char in s1:
    if char in s2:
        print(char)

for index in range(len(s1)):
    if s1[index] in s2:
        print(s1[index])