# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# The smallest number n that is evenly divisible by every number in a set is also known as the lowest common multiple (LCM) of the set of numbers.
# NumPy (Numerical Python) is a Python library used for working with arrays. Numpy has a LCM built in function.
# For more information on Numpy, check david-boo.github.io

import numpy
print(numpy.lcm.reduce(list(range(1,21))))
