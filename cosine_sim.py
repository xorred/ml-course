import numpy as np
import math

raw_input1 = input("Enter numbers separated by spaces: ")
a = np.array(raw_input1.split(), dtype=float)

raw_input2 = input("Enter numbers separated by spaces: ")
b = np.array(raw_input2.split(), dtype=float)

# a = np.array([1,2,3,5])
# b = np.array([3,54,21,4])

ab = np.dot(a,b)

a2 = 0
b2 = 0
for i in range(len(b)):
    a2 = a2 + a[i]*a[i]
    b2 = b2 + b[i]*b[i]


a_sqrt = math.sqrt(a2)
b_sqrt = math.sqrt(b2)

cosine_sim = (ab)/(a_sqrt*b_sqrt)

print(cosine_sim)