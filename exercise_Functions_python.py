#!/usr/bin/env python
# coding: utf-8

# # Questions 1
# # Write a program in Python to make a function that takes a list as an input/argument and returns the sum of all its elements. In the main program,
# # take the list as input from the user, call the function, and substitute the list as
# # the input/argument to the function.

# In[12]:


def sumOfElements(input_list):
    total = 0
    for element in input_list:
        total += element
    return total


input_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
result = sumOfElements(input_list)
print("The sum of the elements is:", result)


# # Questions 2
# # Write a program in Python to make a function that takes a string as an input/argument and returns the string in uppercase. In the main program, take
# # the string as input from the user, call the function, and substitute the string as
# # the input/argument to the function.
# # Output::: Please enter a string: hello world Entered string: hello
# # world Uppercase string: HELLO WORLD

# In[13]:


def to_uppercase(input_string):
    return input_string.upper()

#Rida its main program where program will run
user_input = input("Please enter a string: ")
uppercase_string = to_uppercase(user_input)

print("Entered string:", user_input)
print("Uppercase string:", uppercase_string)


# # Question 3: Write a program in Python to make a function that takes a list as
# # an input/argument and returns a new list with only the even numbers from the
# # original list. In the main program, take the list as input from the user, call the
# # function, and substitute the list as the input/argument to the function.
# # suppose list=[2,3,4,5,6,7,8] new list=[2,4,6,8]

# In[14]:


def filter_even_numbers(input_list):
    even_list = []
    for number in input_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

# Main program
input_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
even_list = filter_even_numbers(input_list)

print("Original list:", input_list)
print("New list with even numbers:", even_list)


# # Questions 4
# # Write a program in Python to make a function that takes a list of integers as
# # an input/argument and returns the maximum value in the list.

# In[15]:


def find_max_value(input_list):
    if not input_list:
        return None  # Return None if the list is empty

    max_value = input_list[0]
    for number in input_list:
        if number > max_value:
            max_value = number
    return max_value

# Main program
input_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
max_value = find_max_value(input_list)

if max_value is not None:
    print("The maximum value in the list is:", max_value)
else:
    print("The list is empty.")


# # Write a program in Python to make a function that takes a list as an input/argument and returns the list sorted in ascending order

# # !st part

# In[16]:


def sort_list_ascending(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(n-1, i, -1):
            if input_list[j] < input_list[j-1]:
                input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
    return input_list

# Main program
input_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
sorted_list = sort_list_ascending(input_list)

print("Original list:", input_list)
print("Sorted list in ascending order:", sorted_list)


# # second method

# In[17]:


def sort_list_ascending(input_list):
    return sorted(input_list)

# Main program
input_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
sorted_list = sort_list_ascending(input_list)

print("Original list:", input_list)
print("Sorted list in ascending order:", sorted_list)

