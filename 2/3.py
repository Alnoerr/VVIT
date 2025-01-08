def is_prime(number):
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))
print(is_prime(21))