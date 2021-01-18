# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Pretty simple code. Create the variable sum and just test every number from 1 to 1000, checking if they are divisible by 3 or 5, if they are, sum them in the variable.

sum = 0
for i in range(1, 1000, 1):
    if (i % 3 == 0) or (i % 5 == 0):
        sum = sum + i
print(sum)
