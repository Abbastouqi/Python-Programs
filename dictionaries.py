#!/usr/bin/env python
# coding: utf-8

# In[21]:


myDict={"name":"abbas","age":24,"gender":"male"}


# In[22]:


myDict["email"]="abbasjkdj@gmail.com"


# In[23]:


myDict


# In[24]:


myDict["age"]=29


# In[25]:


myDict


# In[26]:


myDict["gender"]="female"


# In[27]:


myDict


# # accesing the dictionaries

# In[28]:


print(myDict["name"])


# In[29]:


print(myDict["gender"])


# # removing the items

# In[30]:


del myDict["age"]


# In[31]:


myDict


# # nested dictionaries

# In[41]:


nested_dict={
    "person1":{"name":"abbas","age":20},
    "person2":{"name":"rida","age":17}
            
}


# In[42]:


nested_dict


# In[43]:


stud_dict={
    "rida":["maths","computer","electronics"],
    "abbas":["x","y","z"]
}

print(stud_dict)


# In[ ]:




