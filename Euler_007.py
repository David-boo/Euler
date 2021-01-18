# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# First function just checks if current number is prime. Then it gets stored and prints the 10001th number. Storing the previous numbers is not necessary, just for the sake of it. 
# Can be simplified using libraries that store prime numbers (to do)
# Also Sieve of Eratosthenes could be useful here (to do)


from math import sqrt

counter = 0
prime = 2

def isPrime(num):
    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0 and num != x:
            return False
    return True

while True:
    if isPrime(prime):
        counter += 1
    if counter == 10001:
        print(prime)
        break
    prime += 1
