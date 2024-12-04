def no_of_damaged_dragon(l, m, n, k, d):
	damaged_dragon = 0
	for dragon in range(1,d+1):
		if dragon % l == 0 or dragon%m ==0  or dragon%n==0 or dragon%k==0:
			damaged_dragon +=1
	return damaged_dragon

l = int(input())
m = int(input())
n = int(input())
k = int(input())
d = int(input())
res = no_of_damaged_dragon(l, m, n, k, d)
print(res)