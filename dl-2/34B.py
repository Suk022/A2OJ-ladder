def max_sum_of_money(m, n, data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    max_sum_of_negative = 0
    count = 0
    for num in data:
        if int(num) < 0 and count < int(n):
            max_sum_of_negative += int(num)
            count += 1

    return abs(max_sum_of_negative)

m, n  = input().split()
data = list(map(int, input().split()))
res = max_sum_of_money(m, n, data)
print(res)