#!/usr/bin/env python
# coding: utf-8

# # Two types of loops

# # For Loop
# 

# # While loop

# In[7]:


for i in range(4):  # outer loop
    print("\n",i)
    for j in range(1,4):   #inner loop
        print(j)


# In[9]:


x=[1,3]
y=[3,5]

for i in x:
    for j in y:
        print(i,j)


# In[17]:


for i in  range(2,4):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
        


# In[19]:


list1=[[j for j in range(3)]]
for i in range(5):
    print(list1)


# In[21]:


print("string iteration")

s="python"
for i in s:
    print(i)
    


# In[26]:


for i in range(0,100,20):
    print(i)


# In[30]:


list2=["eat","sleep","happy"]
for count,ele in enumerate(list2):
    print(count,ele)


# In[35]:


for i in range(2,6):
    for j in range(2,6):
        print(i,j)


# In[42]:


number=[x for x in range(11)]

print(number)


# In[48]:


t=((1,2),(3,4),(5,6))
for a,b in t:
    print("a","b")
    print(a,b)


# In[55]:


x=5

while x<=5:
    print(x)
    x+=1


# In[78]:


for i in range(5,0,-2):
    for j in range(i):
        print("*",end="")
    print()


# In[92]:


n=5
for i in range(n,0,-1):
    for j in range(i):
        print(i)
  
        print("*",end="")
    print()


# In[95]:


n=5
for i in range(n,0,-1):
    for j in range(i):
        #print(i)
  
        print("*",end="")    #end will indicate next line
    print()


# In[96]:


n=5
for i in range(n,0,-1):
    for j in range(i):
        #print(i)
  
        print("*")    #end will indicate next line..if you don't use the end line
    print()


# In[91]:


def print_diamond(n):
    # Print the upper half of the diamond
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    
    # Print the lower half of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")
        print()

# Input number of rows for the upper half of the diamond
n = int(input("Enter the number of rows for the upper half of the diamond: "))
print_diamond(n)


# In[97]:


ex[lanation above code
   Here's the code:

python
Copy code
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i)
        print("*", end="")
    print()
Explanation
Setting the value of n:

python
Copy code
n = 5
This sets n to 5. This value determines the size of the pattern.

Outer Loop:

python
Copy code
for i in range(n, 0, -1):
This loop starts with i = n and decrements i by 1 in each iteration until it reaches 1.
The range(n, 0, -1) generates a sequence of numbers from n to 1 (inclusive).
Inner Loop:

python
Copy code
for j in range(i):
For each value of i from the outer loop, the inner loop runs i times.
If i = 5, the inner loop will run 5 times; if i = 4, it will run 4 times, and so on.
Print Statements Inside the Inner Loop:

python
Copy code
print(i)
print("*", end="")
print(i) prints the current value of i and moves to the next line.
print("*", end="") prints a * without moving to the next line due to the end="" argument.
New Line After Inner Loop:

python
Copy code
print()
This print() statement is outside the inner loop but inside the outer loop.
It prints a newline character, moving the cursor to the next line after the inner loop completes.
Detailed Execution:
Let's go through each iteration:

First Iteration (i = 5):

Inner loop runs 5 times (j = 0 to j = 4).
Prints 5 and * 5 times, each on a new line followed by a *:
markdown
Copy code
5
*
5
*
5
*
5
*
5
*
Second Iteration (i = 4):

Inner loop runs 4 times (j = 0 to j = 3).
Prints 4 and * 4 times, each on a new line followed by a *:
markdown
Copy code
4
*
4
*
4
*
4
*
Third Iteration (i = 3):

Inner loop runs 3 times (j = 0 to j = 2).
Prints 3 and * 3 times, each on a new line followed by a *:
markdown
Copy code
3
*
3
*
3
*
Fourth Iteration (i = 2):

Inner loop runs 2 times (j = 0 to j = 1).
Prints 2 and * 2 times, each on a new line followed by a *:
markdown
Copy code
2
*
2
*
Fifth Iteration (i = 1):

Inner loop runs 1 time (j = 0).
Prints 1 and * 1 time, each on a new line followed by a *:
markdown
Copy code
1
*
Complete Output:
Combining all iterations, the output is:

markdown
Copy code
5
*
5
*
5
*
5
*
5
*
4
*
4
*
4
*
4
*
3
*
3
*
3
*
2
*
2
*
1
*
This code prints the value of i followed by a * for each iteration of the inner loop, resulting in a pattern that looks like a descending staircase with each step decorated with a *. If you want to print a diamond pattern, you'll need to modify the code to handle spaces and proper alignment of *.


# In[10]:


n=int(input("enter the number of rows"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[11]:


n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()


# In[13]:


n=int(input("enter the number of rows"))
for i in range(n,0,-2):
    for j in range(1,i+1):
        print("*",end="")
    print()

