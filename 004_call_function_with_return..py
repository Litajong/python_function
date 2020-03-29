#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Call function with return
# return keyword in a function returns a value after exiting the function

def msg_double(phrase):
    double = phrase + " " + phrase
    return double

msg_2x = msg_double("let's go")
print(msg_2x)
type(msg_double("let's go"))


# In[7]:


def half_value(value):
    return value/2

print(half_value(42))


# In[11]:


# Task :Doctor: a function that adds the "Doctor" title to a name
# Define function make_doctor()  that takes a parameter name
# get user input for variable full_name
# call the function using full_name   as argument
# print the return value
# create and call make_doctor() with full_name argument from user input - then print the return value

def make_doctor():
    full_name = input("Enter your full name: ")
    return full_name

print("Doctor name is", make_doctor())


# In[ ]:




