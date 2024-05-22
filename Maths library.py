#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[8]:


num=input("enter the number")

num1=float(num)
sqr_num=math.sqrt(num1)

print("square root of this number ::::",sqr_num)


# In[11]:


num=2.2
print("ceiling of ",num,"is =",math.ceil(num))
print("floor of ",num,"is =",math.floor(num))


# In[18]:


num=5
print("factorial of",num,"is \t" ,math.factorial(num))


# In[19]:


angle=10
print("hyperbola sine of",angle,"is",math.sinh(angle))


# In[20]:


num=10
print("natural log of",num,"is",math.log(num))


# In[21]:


num=10
print("base 10  log of",num,"is",math.log10(num))


# In[22]:


print("value of pi",math.pi)


# In[24]:


base=2
exponential=3
print(base,"raised to the power",exponential,"is =",math.pow(base,exponential))


# In[31]:


import maths   #handler

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

y = b**2 - 4*a*c

if y > 0:
    z = (-b + math.sqrt(y)) / (2 * a)
    w = (-b - math.sqrt(y)) / (2 * a)
    print(f"The roots are real and distinct: {z} and {w}")
elif y == 0:
    root = -b / (2 * a)
    print(f"The root is real and repeated: {root}")
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-y) / (2 * a)
    print(f"The roots are complex and imaginary: {real} + {imaginary}i and {real} - {imaginary}i")

