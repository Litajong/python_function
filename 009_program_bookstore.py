#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program: bookstore()
# create and test bookstore()

# - bookstore() takes 2 string arguments: book & price
# - bookstore returns a string in sentence form
# - bookstore() should call title_it_rtn() with book parameter
# - gather input for book_entry and price_entry to use in calling bookstore()
# - print the return value of bookstore()
# - example of output:Title: The Adventures Of Sherlock Holmes, costs $12.99



# In[6]:


# [ ] create, call and test bookstore() function

def title_it_rtn(msg):
    return msg.title()

def bookstore(book, price):
    form = ("Title: " + title_it_rtn(book) + ", costs $" + price)
    return form
book_entry = input("Enter book title: ")
price_entry = input("Enter book Price: ")

bookstore(book_entry, price_entry)

