def primes(limit):
    # Step 1: create a boolean array
    is_prime = [True] * (limit + 1)
    is_prime[0] = False # 0 is not a prime number
    is_prime[1] = False # 1 is not a prime number

    # Step 2: Sieve process
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Mark multiples of p as non-prime
            for multiple in range(p*p, limit+1, p):
                is_prime[multiple] = False 
        p += 1

    # Step 3: collect all primes
    return [e for e in range(2, limit+1) if is_prime[e]]
