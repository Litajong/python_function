#!/usr/bin/env python
# coding: utf-8

# In[1]:


# String Comparison

# Strings can be equal == or unequal !=
# Strings can be greater than > or less than <
# alphabetically "A" is less than "B"
# lower case "a" is greater than upper case "A"


# In[5]:


"hello" < "Hello"


# In[6]:


"Aardvark" > "Zebra"


# In[7]:


'student' != 'Student'


# In[8]:


print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')


# In[10]:


"Hello " + "World!" == "Hello World!"


# In[14]:


# Task

msg = "Hello"

# [ ] print the True/False results of testing if msg string equals "Hello" string
if msg == "Hello":
    print("True")
else: 
    print("False")


# In[18]:


greeting = "Hello"

# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
msg = input("Say Hello:")

# [ ] print the results of testing if msg string equals greeting string
if msg == greeting:
    print('msg string "equals" greeting string')
else:
    print('msg string "not equal" greeting string')


# In[ ]:




