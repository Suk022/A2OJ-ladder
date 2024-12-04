def amazing_performance(arr):
    min = arr[0]
    max = arr[0]
    extra_ordinary = 0
    if len(arr) == 1 :
        return 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            extra_ordinary +=1
        elif arr[i] > max:
            max = arr[i]
            extra_ordinary +=1

    return extra_ordinary


n = int(input())
arr = list(map(int, input().split()))
res = amazing_performance(arr)
print(res)

