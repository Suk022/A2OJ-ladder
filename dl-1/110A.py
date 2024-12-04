def is_lucky_number(n):
    arr = list(n)
    count = 0
    for i in range(len(arr)):
        if arr[i] == '4' or arr[i] == '7':
            count +=1

    if count == 4 or count == 7:
        return 'YES'
    else:
        return 'NO'

n = input()
res = is_lucky_number(n)
print(res)