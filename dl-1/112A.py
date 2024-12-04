def compare_string_lexicographically(string1 ,string2):
    i = 0
    while (i < len(string1) and i <len(string2)):
        if string1[i].lower() == string2[i].lower:
                i +=1
        else:
            if ord(string1[i]) > ord(string2[i]):
                return 1
            else:
                return -1



string1 = input()
string2 = input()
result = compare_string_lexicographically(string1 ,string2)
print(result)
