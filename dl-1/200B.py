def orange_vol(n, vol):
    queue = list(vol)
    orange_vol_sum = 0
    for vol in queue:
        orange_vol_sum += int(vol)

    result = ((orange_vol_sum / 100) / n) * 100

    print(f"{result:.12f}")

n = int(input())
vol = input().split()
orange_vol(n, vol)
