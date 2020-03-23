#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Program: fishstore()
# create and test fishstore()

# - fishstore() takes 2 string arguments: fish & price
# - fishstore returns a string in sentence form
# - gather input for fish_entry and price_entry to use in calling fishstore()
# - print the return value of fishstore()
# - example of output: Fish Type: Guppy costs $1


# In[7]:


def fishstore(fish , price):
    return("Fish Type: " + fish + " costs $" + price)

def get_fish():
    fish_entry = input("enter fish type: ")
    return fish_entry

def get_price():
    price_entry = input("enter fish price: ")
    return price_entry

print(fishstore(get_fish() , get_price()))


# In[4]:


def fishstore(fish , price):
    return("Fish Type: " + fish + " costs $" + price)

fish_entry = input("enter fish type: ")
price_entry = input("enter fish price: ")

fishstore(fish_entry , price_entry)

