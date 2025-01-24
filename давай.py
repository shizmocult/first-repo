def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrom(n):
    reversed = 0
    N = n
    while N > 0:
        d = N % 10
        reversed = reversed * 10 + d
        N = N // 10
    return reversed == n

counter = 0
for i in range(10_000, 20_000):
    if is_prime(i) and is_palindrom(i):
        counter += 1

print(counter)