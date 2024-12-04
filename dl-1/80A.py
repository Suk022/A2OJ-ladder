def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(b):
    primes = []
    for i in range(2, b + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def check_consecutive(a, b, primes):
    if a in primes and b in primes:
        a_index = primes.index(a)
        if a_index + 1 < len(primes) and primes[a_index + 1] == b:
            return 'YES'
    return 'NO'

n = input().split()
a = int(n[0])
b = int(n[1])

prime_numbers = primes_up_to(b)

res = check_consecutive(a, b, prime_numbers)
print(res)
