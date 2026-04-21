def is_prime(n):
    return all(n%i for i in range(2, n))

def fact(n):
    return 1 if n==0 else n*fact(n-1)
