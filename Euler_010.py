# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Check if number is prime and then define range (2-20000000). Sum primes, print.
# See also Euler_007. 

def IsPrime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


a = 0

for i in range(2, 2000000):
    if IsPrime(i):
        a += i

print(a)
