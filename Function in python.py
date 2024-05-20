#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum():
    a=12
    b=12
    c=a+b
    print(c)
      


# In[2]:


sum()


# In[3]:


def sum(a,b):  #parameters
    print(a+b)
    


# In[4]:


sum(12,12)   #arguments


# In[5]:


def sum(a,b):  #parameters
    return a+b


# In[6]:


sum(2,3)


# In[7]:


def sum(a,b):  #parameters
    return a+b
def sub(a,b):  #parameters
    return a-b
def mul(a,b):  #parameters
    return a*b
def div(a,b):  #parameters
    return a/b


# In[8]:


sum(2,3)
sub(4,3)
mul(2,3)
div(4,2)


# In[9]:


def add():
    a=int(input("enter the  a number"))
    b=int(input("enter the b number"))
    print(a+b) 

def sub():
    a=int(input("enter the  a number"))
    b=int(input("enter the b number"))
    print(a-b)

def mul():
    a=int(input("enter the  a number"))
    b=int(input("enter the b number"))
    print(a*b)


def div():
    a=int(input("enter the  a number"))
    b=int(input("enter the b number"))
    if b!=0:
        print(a/b)
    else:
        print("division by user is not allowed")
        
def calculator():
    while True:
        print("\n simple calculator")
        
        print("1,Add")
        print("2,sub")
        print("3,Mul")
        print("4,div")
        
        choice=input("enter the choice(1/2/3/4/5)")
        if choice =="1":
            add()
        elif choice=="2":
            sub()
            
        elif choice=="3":
            mul()
        elif choice=="4":
            div()
        elif choice=="5":
            print("exit")
            
            break
        else:
            print("invalid choice")

        
calculator()
            
        

        
    
    
        
    



    








    
    


# In[10]:


#making a calculator
# ----------------------starting of function------------------------

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):

    if b == 0:

    
     return 'invalid,cannot calculate:'
    return a/b


def remainder(a,b):

    return a%b
#--------------------------ending of function------------------------------

print('the first and second values are ')
a = int(input('Please enter value of a: '))
b = int(input('Please enter value of b: '))



print('Please choose the operation to perform:')
operation=input('the operation is :')
if operation == '+' :
    print('a+b:',add(a,b))
elif operation == '-':
    print('a-b:',subtract(a,b))
elif operation == '*':
    print('a*b:',multiply(a,b)) 
elif operation == '/':
    print('a/b:',divide(a,b)) 
elif operation == '%':
    print('a%b:',remainder(a,b) )


# # another program

# In[11]:


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4', '+', '-', '*', '/'):
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        
            if choice == '1' or choice == '+':
                result = add(a, b)
                print(f"The result is: {result}")
            elif choice == '2' or choice == '-':
                result = subtract(a, b)
                print(f"The result is: {result}")
            elif choice == '3' or choice == '*':
                result = multiply(a, b)
                print(f"The result is: {result}")
            elif choice == '4' or choice == '/':
                result = divide(a, b)
                print(f"The result is: {result}")
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the calculator
calculator()


# In[ ]:





# In[ ]:




