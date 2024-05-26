#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    'name': ['Abbas', 'Rida', 'Fatima', 'Ahsan', 'Amna'],
    'age': [24, 19, 22, 23, 21],
    'grade': ['A', 'B', 'A', 'C', 'B']
}

students = pd.DataFrame(data)
print(students)


# In[2]:


grade_A_of_student=students[students["grade"]=="A"]


# In[3]:


grade_A_of_student


# In[4]:


grade_B_of_student=students[students["grade"]=="B"]


# In[5]:


grade_B_of_student


# # add another name in dict

# In[6]:


import pandas as pd

# Original data dictionary
data = {
    'name': ['Abbas', 'Rida', 'Fatima', 'Ahsan', 'Amna'],
    'age': [24, 19, 22, 23, 21],
    'grade': ['A', 'B', 'A', 'C', 'B']
}

# Adding the new entry to the dictionary
data['name'].append('Ayesha')
data['age'].append(20)  # Assuming Ayesha is 20 years old
data['grade'].append('A')  # Assuming Ayesha's grade is 'A'

# Convert the updated dictionary to a DataFrame
students = pd.DataFrame(data)
print(students)


# In[7]:


students=students[students['grade']=='A']


# In[8]:


students


# In[47]:


import pandas as pd

# Original data dictionary
data = {
    'name': ['Abbas', 'Rida', 'Fatima', 'Ahsan', 'Amna'],
    'age': [24, 19, 22, 23, 21],
    'grade': ['A', 'B', 'A', 'C', 'B']
}

# Adding multiple new entries to the dictionary
new_names = ['aimal', 'Zaheer', 'Shakeel', 'Jameel', 'Zunair']
new_ages = [20, 25, 26, 22, 24]  # Assuming corresponding ages
new_grades = ['A', 'B', 'C', 'A', 'D']  # Assuming corresponding grades

# Use extend to add multiple values
data['name'].extend(new_names)
data['age'].extend(new_ages)
data['grade'].extend(new_grades)

# Convert the updated dictionary to a DataFrame
students = pd.DataFrame(data)
print(students)


# In[ ]:





# In[ ]:





# In[48]:


students=students[students['grade']=='B']


# In[49]:


students


# In[41]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




