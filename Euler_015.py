# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# This is a combinatin problem, you could just use an arithmetic solution such as 40!/(20! * 20!) = 137846528820

# In a more Python oriented way, just use math package.

import math
n = 20
print(int(math.factorial(2*n)/math.factorial(n)/math.factorial(n)))
