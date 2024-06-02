#!/usr/bin/env python
# coding: utf-8

# # Questions 7
# # Write a program in Python to take a list as an input from the user and double
# # each element in the list. a) Do it using a for loop b) Do it using list comprehension
# 

# In[7]:


input_list = input("Enter a list of numbers separated by spaces: ").split()


input_list = [int(x) for x in input_list]




doubled_list = []
for num in input_list:
    doubled_list.append(num * 2)


print("Doubled list (using for loop):", doubled_list)


# # Part -B From comprehension

# In[8]:


input_list = input("Enter a list of numbers separated by spaces: ").split()


doubled_list = [int(x) * 2 for x in input_list]

print("Doubled list (using list comprehension):", doubled_list)


# # Questions 8
# # Write a program in Python to take a list as an input from the user and remove
# # all duplicate elements. a) Do it using a for loop 

# In[12]:


str_list = input("Enter a list of numbers separated by spaces: ").split()


input_list = []
for x in str_list:
    input_list.append(int(x))


unique_list = []


for num in input_list:
    if num not in unique_list:
        unique_list.append(num)


print("List with duplicates removed (using for loop):", unique_list)


# # <!-- Write a program in Python to take a list as an input from the user and find the
# sum of all even numbers in the list. a) Do it using a for loop b) Do it using list
# comprehension and the sum function -->

# In[13]:


# Take input from the user, separated by spaces
input_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers (in three lines)
numbers = []
for x in input_list:
    numbers.append(int(x))

# Initialize the sum of even numbers
even_sum = 0

# Find the sum of all even numbers using a for loop
for num in numbers:
    if num % 2 == 0:
        even_sum += num

# Print the sum of even numbers
print("Sum of all even numbers (using for loop):", even_sum)


# # Using List Comprehension and the sum Function

# In[14]:


# Take input from the user, separated by spaces
input_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers (in three lines)
numbers = []
for x in input_list:
    numbers.append(int(x))

# Find the sum of all even numbers using list comprehension and the sum function
even_sum = sum([num for num in numbers if num % 2 == 0])

# Print the sum of even numbers
print("Sum of all even numbers (using list comprehension):", even_sum)


# # Write a program in Python to take a list as an input from the user and replace
# # each negative number with zero. a) Do it using a for loop b) Do it using list
# # comprehension

# In[15]:


# Take input from the user, separated by spaces
input_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers (in three lines)
numbers = []
for x in input_list:
    numbers.append(int(x))

# Replace each negative number with zero using a for loop
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

# Print the modified list
print("List with negative numbers replaced by zero (using for loop):", numbers)


# # Using List Comprehension

# In[16]:


# Take input from the user, separated by spaces
input_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers (in three lines)
numbers = []
for x in input_list:
    numbers.append(int(x))

# Replace each negative number with zero using list comprehension
modified_list = [num if num >= 0 else 0 for num in numbers]

# Print the modified list
print("List with negative numbers replaced by zero (using list comprehension):", modified_list)


# # Write a program in Python to take a list as an input from the user and reverse
# # the list. a) Do it using a for loop b) Do it using list slicing

# In[17]:


input_list = input("Enter a list of numbers separated by spaces: ").split()


numbers = []
for x in input_list:
    numbers.append(int(x))


reversed_list = []


for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])


print("Reversed list (using for loop):", reversed_list)


# # Using List Slicing

# In[18]:


input_list = input("Enter a list of numbers separated by spaces: ").split()


numbers = []
for x in input_list:
    numbers.append(int(x))


reversed_list = numbers[::-1]


print("Reversed list (using list slicing):", reversed_list)


# # Write a program in Python to take a list as an input from the user and extract all
# # strings from the list. a) Do it using a for loop b) Do it using list comprehension
# 

# In[21]:


input_list = input("Enter a list of elements separated by spaces: ").split()


strings = []
for item in input_list:
    if isinstance(item, str):
        strings.append(item)


print("Strings extracted (using for loop):", strings)


# # Using List Comprehension

# In[22]:


input_list = input("Enter a list of elements separated by spaces: ").split()

strings = [item for item in input_list if isinstance(item, str)]

print("Strings extracted (using list comprehension):", strings)


# # Write a program in Python to take a list as an input from the user and create
# # a new list with the square of each element. a) Do it using a for loop b) Do it
# # using list comprehension

# In[23]:


input_list = input("Enter a list of numbers separated by spaces: ").split()

numbers = []
for x in input_list:
    numbers.append(int(x))

squared_list = []
for num in numbers:
    squared_list.append(num ** 2)

print("New list with the square of each element (using for loop):", squared_list)


# # Using List Comprehension

# In[ ]:


input_list = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(x) for x in input_list]

squared_list = [num ** 2 for num in numbers]

print("New list with the square of each element (using list comprehension):", squared_list)


# In[ ]:




