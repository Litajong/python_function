#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Task: Functions Arguments & Parameters
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme

def short_rhyme():
    print("first", "second", "third", "\nforth", "fifth", "sixth")

my_rhyme = ("You", "love", "me", "and", "I", "love you") 

print(short_rhyme(my_rhyme))


# In[14]:


# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case

def title_it(msg):
    print(msg.title())

my_msg = "today is sunday"
title_it(my_msg)


# In[15]:


# [ ] get user input with prompt "what is the title?" 
# [ ] call title_it() using input for the string argument

my_msg = input("what is the title?")
title_it(my_msg)


# In[18]:


# [ ] define title_it_rtn() which returns a titled string instead of printing

def title_it_rtn(msg):
    return msg.title()


# In[19]:


# [ ] call title_it_rtn() using input for the string argument and print the result
print(title_it_rtn(input()))

