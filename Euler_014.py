# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Creates a Collatz sequence where (excluding 1) if n is even then result is n/2 and if it is odd then result is 3n+1.

# Then, print the longest number that creates the longest sequence.

def Collatz(n):
    count=0
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        count+=1
    return count
maxi=0
maxv=0
for i in range(1,1000000):
    if maxi<Collatz(i):
        maxi=Collatz(i)
        maxv=i
print(maxv)
