# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Define limit and create sum function. While sum is less than limit, add every third number of fib sequence (as they are the even numbers)

limit = 4e6
FIB = [1, 2]
new = sum(FIB)

while new < limit:
        FIB += [new]
        new = FIB[-1] + FIB[-2]

print(sum([-i*(i%2-1) for i in FIB]))
