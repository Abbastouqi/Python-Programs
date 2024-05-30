#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=input("enter the elements of list::")
x=list(map(int , x.split()))

y=[]

for i in x:
    y.append(i/10*100)
    
print("list x:",x)

print("list y:",y)

diction={}

for i in range(len(x)):
    diction[x[i]]=y[i]
    
print("the itemns in dict")
    
print(diction)
    


# In[4]:


x=input("enter the elements of list::")
x=list(map(int , x.split()))
diction={}

for i in range(len(x)):
    diction[x[i]]=y[i]
    
print("the itemns in dict")
    
print(diction)


# In[7]:


x=input("enter the elements of list::")
x=list(map(int , x.split()))

y=[]

for i in x:
    y.append(i/10*100)
    
print("list x:",x)

print("list y:",y)

n=len(x)
for i in range(n//2):
    #reverse of x
    temp=x[i]
    x[i]=x[n-i-1]
    x[n-i-1]=temp
    
    temp=y[i]
    y[i]=y[n-i-1]
    y[n-i-1]=temp
    
    
    
    
    
print("list x:",x)
print("list x:",y)


# In[8]:


for key in diction:
    print(f"key:{key},value :{diction[key]}")


# In[10]:


usr_dict={}
num_pair=int(input("enter the n key value pairs::"))

for i in range(num_pair):
    key=input(f"enter the key {i+1}: ")
    value=input(f"enter the value {key}: ")
    usr_dict[key]=value
    
print("which dic we have taken::")
print(usr_dict)
    


# In[ ]:





# In[ ]:




