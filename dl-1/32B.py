def borze_code(s):
    queue = list(s)
    new_queue = []
    i = 0
    while(i< len(queue)):
        if (queue[i] == '.'):
            new_queue.append('0')
            i +=1
        elif (queue[i] == '-'):
            if (queue[i+1]=='.'):
                new_queue.append('1')
                i +=2
            elif (queue[i+1] == '-'):
                new_queue.append('2')
                i+=2

    return ''.join(new_queue)

s = input()
result = borze_code(s)
print(result)