# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# A factor is a whole number which divides exactly into a whole number, leaving no remainder.

# You can check for Prime numbers by checking every number between 1 and sqrt(number), since the maximum (unique) divisor for any number is its square root.


def factors(x):
    return [i for i in range(1,int(x**0.5)+1) if x%i==0]
num = 0
i = 1
while True:
    num += i
    i += 1
    if len(factors(num))*2 > 500:
        break
print(num)
