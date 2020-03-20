#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Program: bird_available: ask for user to "input a bird name to check for availability" and print a statement informing of availability
# create this program with a Boolean function bird_available()
# has parameter that takes the name of a type of bird
# for this exercise the variable bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
# return True or False (we are making a Boolean function)
# call the function using the name of a bird type from user input
# print a sentence that indicates the availability of the type of bird checked


# In[21]:


# create function bird_available

def bird_available(bird):
    bird_types = 'crow, robin, parrot, eagle, sandpiper, hawk, pigeon'
    return(bird.lower() in bird_types)

# user input
bird_search = input("Enter bird type to search :")

# call bird_available
have_bird = bird_available(bird_search)

# print availability status
print(bird_search, "available is ",have_bird)


# In[22]:


# Task: Fix the error
# define function how_many
how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")


# In[23]:


def how_many():
    requested = input("enter how many you want: ")
    return requested

number_needed = how_many()
print(number_needed, "will be ordered")


# In[ ]:




