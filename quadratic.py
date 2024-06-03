#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None  # No real roots
    sq_rt = math.sqrt(discriminant)
    sol_1 = (-b + sq_rt) / (2*a)
    sol_2 = (-b - sq_rt) / (2*a)
    return sol_1, sol_2

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

sol_1, sol_2 = quadratic_equation(a, b, c)

xoxo = sol_1
yoyo = sol_2

if xoxo is None and yoyo is None:
    print("No real roots")
else:
    print(xoxo)
    print(yoyo)


# # Discriminant: D = b2 - 4ac   D > 0, the roots are real and distinct D = 0, the roots are real and equal.D < 0, the roots do not exist or the roots are imaginary.

# In[12]:


import math

def quadratic_equation(a, b, c):
    z = b**2 - 4*a*c
    if z < 0:
        return None, None 
    
    sq_rt = math.sqrt(z)
    sol_1 = (-b + sq_rt) / (2*a)
    sol_2 = (-b - sq_rt) / (2*a)
    return sol_1, sol_2

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

sol_1, sol_2 = quadratic_equation(a, b, c)

if sol_1 is None and sol_2 is None:
    print("No real roots")
else:
    print(sol_1)
    print(sol_2)


# In[ ]:




