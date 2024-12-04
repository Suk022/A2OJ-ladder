def swap_stones(n):
    arr = list(n)
    swap_need = 0
    if len(arr) == 1:
        swap_need = 0
    i = 0
    while (i < len(arr)-1):
        if arr[i] == arr[i+1]:
            swap_need +=1
        i +=1

    return swap_need

size_of_arr = int(input())
n = input()
if len(n) == size_of_arr:
    res = swap_stones(n)
    print(res)

