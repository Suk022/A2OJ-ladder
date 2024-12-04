def case_convers(s):
    queue =list(s)
    if queue[0].isupper():
        return ''.join(queue)
    elif queue[0].islower():
        queue[0] = queue[0].upper()
        return ''.join(queue)

s = input()
result = case_convers(s)
print(result)