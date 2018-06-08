
# coding: utf-8

# In[8]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('seaborn-notebook')
import warnings
warnings.filterwarnings("ignore")
from dateutil.relativedelta import relativedelta
import datetime
import time


# In[9]:

#1 My name Nick Judson


# In[10]:

#2 Create matrix A with size (3,5) containing random numbers A = np.random.random(15)

A = np.matrix([np.random.random(15)]).reshape(3,5)
A


# In[11]:

#3 Find the size and length of matrix A

len(A)


# In[12]:

A.size


# In[17]:

#4 Resize (crop/slice) matrix A to size (3,4)
# Assuming the sliced output is what is wanted, not just a one off. Therefore overwriting to A

A = np.resize(A,(3,4))
A


# In[48]:

#5 Find the transpose of matrix A and assign it to B

B = A.T
B


# In[19]:

#6 Find the minimum value in column 1 of matrix B (check the properties of a matrix – ‘B.min()’)
# Assuming this means find the minimum of the first column, not column 1

B.min(0)[0]


# In[24]:

#7 Find the minimum and maximum values for the entire matrix A

A.min()


# In[25]:

A.max()


# In[26]:

#8 Create vector X (an array) with 4 random numbers

X = np.array([np.random.random(4)])
X


# In[43]:

#9 Create a function and pass vector X and matrix A in it
#10 In the new function multiply vector X with matrix A and assign the result to D
# (note: you may get an error! ... think why and fix it. Recall matric manipulation in class!)

def my_func(X, A):
    D = X*A
    return(D)
    print(D)

D = my_func(X,A)
D


# In[37]:

#11 Create a complex number Z with absolute and real parts != 0

Z = 2 +1j
Z


# In[40]:

#12 Show its real and imaginary parts as well as it’s absolute value

Z.real
Z.imag
abs(Z)


# In[45]:

#13 Multiply result D with the absolute value of Z and record it to C

C = my_func(X,A) * abs(Z)
C


# In[49]:

#14 Convert matrix B from a matrix to a string and overwrite B

B = str(B.flatten())
B


# In[50]:

#15 Display a text on the screen: ‘Your Name is done with HW2‘

print('Nick Judson is done with HW2')


# In[ ]:



