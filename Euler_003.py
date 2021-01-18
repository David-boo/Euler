# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# The fundamental theorem of arithmetic states that every integer greater than 1 either is a prime number itself or can be represented as the product of prime numbers.
# Check our big number n and divide by its smallest factor (which must also be prime)
# Last factor that we divide out must be the largest prime factor of n.

number = 600851475143
factor = 2

while number != 1:
    if number % factor == 0:
        print(factor)
        number = number / factor
        factor += 1
    else:
        factor += 1

