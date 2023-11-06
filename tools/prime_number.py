def is_prime(prime):
    if prime > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(prime / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (prime % i) == 0:
                print(prime, "is not a prime number")
                break
        print(prime, "is a prime number")
    else:
        print(prime, "is not a prime number")
