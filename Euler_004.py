# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Quite straightforward. Define range (100-1000), multiply and check if they are palindromic. If they are, store them in a list and print the max number.

num = []
for a in range(100,1000):
     for b in range(100,1000):
               m = a*b
               if str(m) == str(m)[::-1]:
                    num.append(int(m))

print(max(num))
