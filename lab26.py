import numpy as np
from oauthlib.oauth2.rfc6749.tokens import random_token_generator

#2-1 a = np.arange(10)
# print(a)
#
#2-2
# bool_arr=np.array((2,2),dtype=bool)
# print(bool_arr)
#
#2-3
# arr=np.arange(1,51)
# prime_arr = arr[[x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) for x in arr]]
# print(prime_arr)
#2-4
# a=np.random.randint(1,20,size=20)
# print("***** 1D array with 20 random elements*****")
# print(a)
# A=a.reshape(4,5)
# print("*** 4*5 array ***")
# print(A)

#2-5
#Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has
#only 1s. Then stack the two arrays horizontally

# a=np.arange(10)
# b=np.ones(10, dtype=int)
# d=np.hstack((a,b))
# print(d)

#2-6
#Define two 1D arrays, where array a has list of first 100 numbers, and b has first
# 100 prime numbers. Obtain a new array that is the intersection of these two
# arrays (Hint: use np.intersect1d())

# arr1=np.arange(101)
# # # print(arr1)
# arr2= arr1[[x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) for x in arr1]]
# arr3=np.intersect1d(arr1,arr2)
# print(arr3)

#2-7
# Use the above two arrays with the aim this time to remove items from a that are
# in b. (We are doing a-b operation, use np.setdiff1d())

# c=(np.setdiff1d(arr1,arr2))
# print(c)

#2-8
# arr= np.where(np.isin(arr1, arr2))[0]
# print(arr)

#2-9
# Extract the elements of the array a above that are greater than 5 and less than
# 20.
# extract=arr1[(arr1>5) & (arr1<20)]
# print(extract)


# import numpy as np
#
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
#
# # Reverse rows
# reverse_rows = arr[::-1, :]
#
# # Reverse columns
# reverse_columns = arr[:, ::-1]
#
# print("Original:")
# print(arr)
#
# print("Reversed rows:")
# print(reverse_rows)
#
# print("Reversed columns:")
# print(reverse_columns)
#
#
#
# import numpy as np
#
# arr = np.random.randint(1, 100, (3, 3))
#
# print("Original matrix:")
# print(arr)
#
# arr[:, [0, 1]] = arr[:, [1, 0]]
#
# print("After swapping columns:")
# print(arr)
#
#
# import numpy as np
#
# def maximum_array(a, b):
#
#     c = np.maximum(a, b)
#
#     return c
#
#
# a = np.array([1, 2])
# b = np.array([0, 5])
#
# c = maximum_array(a, b)
#
# print(c)
#
#
# import numpy as np
#
# np.set_printoptions(precision=3)
#
# arr = np.random.rand(3, 3)
#
# print(arr)
#
#
#
# import numpy as np
#
# np.set_printoptions(suppress=True)
#
# arr = np.array([10000000000, 20000000000, 30000000000])
#
# print(arr)
#
#
#
# import numpy as np
#
# arr = np.array([10, 25, 30, 15, 40, 18, 50, 12, 35, 22])
#
# print("Average:", np.mean(arr))
#
# print("Highest:", np.max(arr))
#
# print("Lowest:", np.min(arr))
#
# print("Numbers above 20:", arr[arr > 20])
#
# print("Count above 20:", np.sum(arr > 20))
#
# print("Numbers below 20:", arr[arr < 20])
#
#
#
# import numpy as np
#
# counts = np.array([100, 200, 300, 400, 500])
#
# # Calculate log2 of each count
# log_values = np.round(np.log2(counts), 2)
#
# # Calculate percentage of total
# percentages = np.round((counts / np.sum(counts)) * 100, 1)
#
# print("Gene counts:", counts)
#
# print("Log2 values:", log_values)
#
# print("Percentages:", percentages)
#
#
#
# import numpy as np
#
# # Time points
# t = np.arange(0, 121, 20)
#
# # Calculate population
# population = 100 * 2**(t / 20)
#
# print("Time:", t)
#
# print("Population:", population)
#
# # How many times larger is the final population?
# ratio = population[-1] / population[0]
#
# print("Final population is", ratio, "times larger")
#
# # Find time points where population is above 1000
# result = t[population > 1000]
#
# print("Time points above 1000:", result)
#
#
#
# import numpy as np
#
# dna = "GATTACA"
#
# mapping = {
#     "A": [1, 0, 0, 0],
#     "C": [0, 1, 0, 0],
#     "G": [0, 0, 1, 0],
#     "T": [0, 0, 0, 1]
# }
#
# encoded = np.array([mapping[base] for base in dna])
#
# print("DNA sequence:", dna)
#
# print("One-hot encoded matrix:")
# print(encoded)
#
#
#
# import numpy as np
#
# # Create a 5 x 10 matrix
# expression = np.random.rand(5, 10) * 100
#
# print("Original expression matrix:")
# print(expression)
#
# # Calculate mean of each row
# row_mean = np.mean(expression, axis=1, keepdims=True)
#
# # Subtract row mean
# normalized = expression - row_mean
#
# print("Normalized matrix:")
# print(normalized)
#
# # Calculate total expression of each sample
# column_sum = np.sum(normalized, axis=0)
#
# print("Column sums:")
# print(column_sum)
#
# # Set threshold
# threshold = 50
#
# # Find samples above threshold
# samples = np.where(column_sum > threshold)
#
# print("Samples above threshold:")
# print(samples)


