# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Note that we are defining a just as the difference between 1000 (total) and b-c

for c in range(1,1000):
    for b in range(1,1000):
       if  10**6-2*(10**3)*(b+c) +2*b**2 +2*b*c==0 and b<c:
           if b+c<1000:
                print("a :",1000-b-c,"b:",b,"c :",c,"a*b*c :",b*c*(1000-b-c))
