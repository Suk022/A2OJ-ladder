def max_sum_of_money(arr,n):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    max_sum_of_negative = 0
    count = 0
    for num in arr:
        if int(num) < 0 and count < int(n):
            max_sum_of_negative += int(num)
            count += 1

    return abs(max_sum_of_negative)


m, n = map(int, input().split())
arr = list(map(int, input().split()))
res = max_sum_of_money(arr, n)
print(res)