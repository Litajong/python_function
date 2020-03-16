#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Default Arguments
# Default Arguments are used if no argument is supplied
# Default arguments are assigned when creating the parameter list

def say_this(phrase = "Hi"):  
      print(phrase)

say_this()


# In[3]:


# yell_this() yells the string Argument provided

def yell_this(phrase):
    print(phrase.upper() + "!")

# call function with a string
yell_this("It is time to save the notebook")


# In[7]:


# use a default argument
def say_this(phrase = "Hi"):  
    print(phrase)
    
say_this()
say_this("Bye")


# In[8]:


# Task: Define yell_this() and call with variable argument

words_to_yell = input()

yell_this(words_to_yell)

