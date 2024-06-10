#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# random vector of size 15 with integers in the range 1-20
random_vector = np.random.randint(1, 21, size=15)
print("Original Vector: \n", random_vector)

# reshape the vector to 3 by 5 array
reshape_array = np.reshape(random_vector, (3, 5))
print("Reshaped Array: \n", reshape_array)

# print the shape of the array
print("Shape of the Array: ", reshape_array.shape)

# replace the max in each row by 0
max= np.argmax(reshape_array, axis=1)
for i in range(reshape_array.shape[0]):
    reshape_array[i, max[i]] = 0
print("Array after replacing max in each row by 0: \n", reshape_array)

# 2-dim array of size 4 x 3 with 4-byte integer elements
new_array = np.zeros((4, 3), dtype=np.int32)
print("New Array: \n", new_array)
print("Shape of New Array: ", new_array.shape)
print("Type of New Array: ", type(new_array))
print("Data type of New Array: ", new_array.dtype)


# In[2]:


#b
import numpy as np
from numpy.linalg import eig

#  input matrix
A = np.array([[3, -2], [1, 0]])

# the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues: ", eigenvalues)
print("Right eigenvectors: \n", eigenvectors)


# In[3]:


#c
import numpy as np

#  input array
arr = np.array([[0, 1, 2], [3, 4, 5]])

# sum of diagonal elements
sum_diag = np.trace(arr)

print("Sum of diagonal elements: ", sum_diag)


# In[4]:


#d
import numpy as np

# input array
arr = np.array([[1, 2], [3, 4], [5, 6]])

#actual input of the array 
print("Given input array: \n", arr)

# reshape to 2x3
arr= np.reshape(arr, (2, 3))
print("Reshape to 2x3: \n", arr)


# In[5]:


#d
import matplotlib.pyplot as plt

# given data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# display the  pie chart
plt.pie(popularity, labels=languages,explode=(0.1,0,0,0,0,0),autopct='%1.1f%%',startangle=90)

# show the chart
plt.show()


# In[ ]:




