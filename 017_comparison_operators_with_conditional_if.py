#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Comparison Operators in Conditionals "if"

x = 21

if x > 25:
    print("x is already bigger than 25")
else:
    print("x was", x)
   


# In[3]:


x = 53

if x > 57:
    print("x is already bigger than 57")
else:
    print("x was", x)
    x = 68
    print("now x is", x)


# In[6]:


position = 16
trap_value = 16

if position != trap_value:
    print("....keep playing!")
else:
    print("Position is", trap_value, "....GAME OVER!")


# In[17]:


# DON'T ASSIGN (x = 2) when you mean to COMPARE (x == 2)

x = 2

if x == 2:
    print('"==" tests for, "is equal to"')
else:
    pass


# In[10]:


x = 18
if x + 18 == x + x:
    print("Pass: x + 18 is equal to", x + x)
else:
    print("Fail: x + 18 is not equal to", x + x)


# In[15]:


x = 18
test_value = 18

if x != test_value:
    print('x is not', test_value)
else:
    print('x is', test_value)


# In[25]:


# Task
# [ ] create an if/else statement that tests if y is greater than or equal x + x 
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output

x = 8
y = x + 8

if y >= x + x:
    print("y greater than or equal x + x is", y >= x + x)
else:
    print("y greater than or equal x + x is", y >= x + x)

