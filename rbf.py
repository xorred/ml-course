import numpy as np
import math

raw_input1 = input("Enter numbers separated by spaces: ")
a = np.array(raw_input1.split(), dtype = float)

raw_input2 = input("Enter numbers separated by spaces: ")
b = np.array(raw_input2.split(), dtype = float)

gamma = float(input("Enter the value of gamma: "))
if(gamma <=0):
    print("gamma should be greater than 0")
else:
    a_b_diff =np.linalg.norm(a - b)
    a_b = np.exp(-gamma * (a_b_diff **2))
    print("RBF Similarity between the two vectors is: ", a_b)