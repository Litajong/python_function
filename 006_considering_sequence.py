#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Considering Sequence
# Function definitions are placed at the beginning of a page of code.

have_hat = hat_available('green')  
  
print('hat available is', have_hat)

def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)
    
# This results in an error - the code flows from top to bottom is in the incorrect sequence
# NameError: name 'hat_available' is not defined
# In the statement have_hat = hat_available('green') the function hat_available() needs to be called after the function has been defined


# In[5]:



def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)
    
have_hat = hat_available('green')  

print('hat available is', have_hat)

