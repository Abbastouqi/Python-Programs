#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random

y=random.randint(1,10)
print(y)


# In[33]:


import random

y=random.random()
print(y)


# In[39]:


item=["apple","banaana","cheery","orange"]
random_item=random.choice(item)
print(random_item)


# In[44]:


deck=list(range(1,53))

random.shuffle(deck)
print(deck)


# In[50]:


random.seed(50)

print(random.random())


# In[63]:


import random



def generate_random_integer():
    x = int(input("Enter the x number: "))
    y = int(input("Enter the y number: "))
    return random.randint(x, y)

def generate_random_float():
    return random.random()

def main():
    print("Choose the option:")
    print("1. Generate a random integer")
    print("2. Generate a random float")
    
    choice = int(input("Enter the choice (1 or 2): "))
    
    if choice == 1:
        print("Random integer:", generate_random_integer())
    elif choice == 2:
        print("Random float:", generate_random_float())
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


# In[64]:


def divide():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if b != 0:
        print(f"The quotient of {a} divided by {b} is {a / b}")
    else:
        print("Error: Division by zero is not allowed")

divide()  # Example call


# In[ ]:





# In[ ]:




