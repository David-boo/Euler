# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Again straightforward. Define function as the sum of the squares and the square of the sum and apply to 100.
# Doesn't take too long but could be resolved in a more mathematical approach defining n(n+1)/2 and n(n+1)(2n+1)/6  (to-do?)

def diff(n):
    return sum(range(1,n+1))**2 - sum([i**2 for i in range(1,n+1)])

diff(100)
