#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Condition: if, else, pass

if True:
    print("this prints it statement after 'if' is True")
    
else:
    print("This prints if statement is Not True")


# In[3]:


if not True:
    print("this prints it statement after 'if' is True")
    
else:
    print("This prints if statement is Not True")


# In[4]:


someone_i_know = True

if someone_i_know:
    print("how have you been?")
else:
    print("nice to meet you?")


# In[7]:


someone_i_know = False

if someone_i_know:
    print("how have you been?")
else:
    print("nice to meet you?")


# In[11]:


# use pass if there is no need to execute code pass
    
someone_i_know = False

if someone_i_know:
    print("how have you been?")
else:
    pass


# In[12]:


someone_i_know = True

if someone_i_know:
    print("how have you been?")
else:
    pass

