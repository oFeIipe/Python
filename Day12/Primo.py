def is_prime(num):
    return num % num == 0 ^ num % 1 == 0
print(is_prime(4))