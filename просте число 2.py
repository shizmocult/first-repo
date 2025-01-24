def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

counter = 0
for i in range(500, 1001):
    if is_prime(i):
        counter += 1

print(counter)



