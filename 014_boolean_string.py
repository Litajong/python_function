#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Using Conditionals with Boolean String test methods
# if student_name.isalpha():
# .isalnum()
# .istitle()
# .isdigit()
# .islower()
# .startswith()


# In[3]:


# review code and run cell

favorite_book = input("Enter the title of a favorite book: ")

if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
    
else:
    print(favorite_book, "- consider capitalization throughout for book title.")
    


# In[4]:


favorite_book = input("Enter the title of a favorite book: ")

if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
    
else:
    print(favorite_book, "- consider capitalization throughout for book title.")


# In[8]:


a_number = input("enter a positive integer number: ")

if a_number.isdigit():
    print(a_number, "is a positive integer")
else:
    print(a_number, "is not a positive integer")


# In[13]:


# another if

an_alpha = input("enter a word: ")

if an_alpha.isalpha():
    print(an_alpha, "is more like a word")
else:
    pass


# In[15]:


# review code and run cell
vehicle_type = input('"enter a type of vehicle that starts with "P": ')

if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


# In[ ]:




