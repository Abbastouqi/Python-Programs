#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits=["gauva","apple","mango","orange","happy"]

print(fruits)


# In[2]:


len(fruits)


# In[3]:


fruits


# In[4]:


for fruit in fruits:
    print(fruit)    


# In[5]:


fruits[-3]


# In[6]:


mixed_list=["apple",1,'orange',3,4,5]
print(mixed_list)


# In[7]:


mixed_list[-1]


# In[8]:


for mixed in mixed_list:
    print(mixed)


# In[9]:


fruits[3]="blueberry"


# In[10]:


fruits


# In[11]:


mixed_list[5]="blueberry"


# In[12]:


mixed_list


# In[13]:


mixed_list.append("peech")


# In[14]:


mixed_list


# In[15]:


mixed_list.insert(1,"peech")


# In[16]:


print(mixed_list)


# In[17]:


list1=[1,"age",2,3,4]
list2=[3,4,5,6,"female"]

combine=list1+list2


# In[18]:


combine


# In[19]:


fruits.remove("apple")


# In[20]:


print(fruits)


# In[21]:


fruits.insert(1,"apple")


# In[22]:


fruits


# In[23]:


fruits_two=fruits.pop(1)


# In[24]:


fruits_two


# # fruits

# # slicing in list

# In[25]:


sublist=fruits[1:4]


# In[26]:


sublist


# In[27]:


fruits


# # dictionaries in lists

# In[28]:


student=[
    {"name":"alice","age":23,"major":"physics"},
    {"name":"BOB","age":22,"major":"maths"},
    {"name":"charlie","age":20,"major":"computer science"}
    
]


# In[29]:


student


# In[30]:


new_student={"name":"david","age":44,"major":"biology"}


# In[31]:


student.append(new_student)


# In[32]:


print(student)


# In[33]:


for students in student:
    print(f:"name":  {student["age"]},major:{student["major"]}"}


# In[ ]:


matrix=[
    [1,2,3],
    [2,3,4],
    [3,4,5]
]


# In[ ]:


print(matrix)


# In[ ]:


for i in matrix:
    print(i)


# In[ ]:


element=matrix[1][2]


# In[ ]:


element


# In[ ]:


element=matrix[2][2]


# In[ ]:


element


# In[37]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")
# Split the input string into individual elements and convert them to a list
user_list = user_input.split()

# Print the list
print("The list you entered is:", user_list)




# In[39]:





# In[40]:





# In[42]:


# Prompt the user to enter integers separated by spaces
user_input = input("Enter the integers of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of integers
user_list = list(map(int, user_input.split()))


# In[45]:


# Predefined list of integers
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Create a new list to store even numbers
odd_list = []

# Iterate through the user list and add only even numbers to the new list
for num in user_list:
    if num % 2 ==1:
        odd_list.append(num)

# Print the list with odd numbers removed
print("The list with odd numbers removed is:", odd_list)


# # take dic from user

# In[1]:


# Initialize an empty list to store student dictionaries
students = []

# Number of students
num_students = 3

# Loop to gather data for each student
for i in range(num_students):
    print(f"Enter details for student {i + 1}:")
    
    # Create an empty dictionary for the student
    student_dict = {}
    
    # Get user input for each key-value pair
    student_dict["name"] = input("Name: ")
    student_dict["age"] = int(input("Age: "))
    student_dict["major"] = input("Major: ")
    
    # Append the student dictionary to the list
    students.append(student_dict)

# Print the list of student dictionaries
print("Student details:")
print(students)


# In[2]:


# Initialize an empty list to store student dictionaries
students = []

# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students: "))

# Loop to gather data for each student
for i in range(num_students):
    print(f"Enter details for student {i + 1}:")
    
    # Create an empty dictionary for the student
    student_dict = {}
    
    # Get user input for each key-value pair
    student_dict["name"] = input("Name: ")
    student_dict["age"] = int(input("Age: "))
    student_dict["major"] = input("Major: ")
    
    # Append the student dictionary to the list
    students.append(student_dict)

# Print the list of student dictionaries
print("Student details:")
print(students)


# In[3]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[4]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of integers
user_list = list(map(int, user_input.split()))

# Create a new list to store even numbers
even_list = []

# Iterate through the user list and add only even numbers to the new list
for num in user_list:
    if num % 2 == 0:
        even_list.append(num)

# Print the list with odd numbers removed
print("The list with odd numbers removed is:", even_list)


# In[6]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of integers
user_list = list(map(int, user_input.split()))

# Iterate through the user list and print only the even numbers
print("The even numbers are:")
for num in user_list:
    if num % 2 == 0:
        print(num)


# In[7]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of floats
user_list = list(map(float, user_input.split()))

# Create a new list to store integers
integer_list = []

# Iterate through the user list and add only integers to the new list
for num in user_list:
    if num.is_integer():
        integer_list.append(int(num))

# Print the list with floats removed
print("The list with floats removed is:", integer_list)


# In[8]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of floats
user_list = list(map(float, user_input.split()))

# Use list comprehension to create a new list with only integers
integer_list = [int(num) for num in user_list if num.is_integer()]

# Print the list with floats removed
print("The list with floats removed is:", integer_list)


# In[10]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements and convert them to a list of integers
user_list = list(map(int, user_input.split()))

# Sort the list in descending order
user_list.sort(reverse=True)

# Print the sorted list
print("The list sorted in descending order is:", user_list)


# In[12]:


# Prompt the user to enter elements separated by spaces
user_input = input("Enter the elements of the list separated by spaces: ")

# Split the input string into individual elements
input_list = user_input.split()

# Convert each element to an integer using a list comprehension
integer_list = [int(element) for element in input_list]

# Print the list of integers
print("The list with elements converted to integers is:", integer_list)


# In[ ]:




