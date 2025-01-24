def is_prime (n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
counter = 0
for i in range(1000, 10000):
    if is_prime (i):
        counter = counter + 1
print(counter)