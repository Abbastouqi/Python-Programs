#!/usr/bin/env python
# coding: utf-8

# # LIST IN PYTHON

# # Creating the list

# In[33]:


fruits=["amrod","apple","mango","orange","happy"]
print(fruits)


# # Loop in list

# In[34]:


for fruit in fruits:
    print(fruit)


# # How we can access element by index

# In[35]:


fruits[0]


# In[36]:


fruits[-2]


# # Mixed data types in a list

# In[37]:


mixed_list=["apple",1,"banna",2,3,"mango"]
mixed_list


# In[38]:


for mixed in mixed_list:
    print(mixed)


# # . #Modifying Elements

# In[39]:


mixed_list[0]="blueberry"


# In[40]:


mixed_list


# In[41]:


mixed_list[3]="blueberry"


# In[42]:


mixed_list


# # Adding Elements

# In[43]:


mixed_list.append("peech")


# In[44]:


mixed_list


# In[45]:


mixed_list.insert(0,"peech")


# In[46]:


mixed_list


# In[47]:


mixed_list.insert(1,"avagado")


# In[48]:


mixed_list


# In[49]:


len(mixed_list)


# In[50]:


mixed_list[5]


# # Removing the element

# In[51]:


fruits.remove("apple")


# In[52]:


fruits


# In[53]:


fruits.insert(1,"apple")


# In[54]:


fruits


# In[55]:


fruits_tw0=fruits.pop(1)


# In[56]:


fruits


# In[57]:


fruits_tw0


# # slicing in list

# In[64]:


sublist = fruits[2:5]


# In[65]:


fruits


# In[66]:


sublist


# # Creating a List of Dictionaries

# In[67]:


students = [
    {"name": "Alice", "age": 21, "major": "Physics"},
    {"name": "Bob", "age": 22, "major": "Mathematics"},
    {"name": "Charlie", "age": 20, "major": "Computer Science"}
]


# In[68]:


print(students)


# In[69]:


students


# # Adding a New Dictionary to the List

# In[70]:


new_student = {"name": "David", "age": 23, "major": "Biology"}
students.append(new_student)


# In[71]:


new_student


# In[72]:


students


# In[79]:


for student in students:
    print(f"age: {student['age']},Major: {student['major']}")


# # Creating a nested list

# In[80]:


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [3, 4, 5]
]

# Accessing elements in a nested list
element = matrix[3][2]  


# In[81]:


element


# In[86]:


for matrixs in matrix:
    print("It will print all  lists:")
    print(matrixs)


# In[ ]:




