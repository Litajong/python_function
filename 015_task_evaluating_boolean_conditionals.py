#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task: Evaluating Boolean Conditionals
# create evaluations for .islower()
# - print output describing if each of the 2 strings is all lower or not

test_string_1 = "welcome"
test_string_2 = "I have $3"

# [ ] use if, else to test for islower() for the 2 strings

if test_string_1.islower():
    print(test_string_1 + " is all lower")
else:
    print(test_string_1 + " is not all lower")
    
if test_string_2.islower():
    print(test_string_2 + " is all lower")
else:
    print(test_string_2 + " is not all lower")    


# In[16]:


# Task continued
# create a functions using startswith('w')
# w_start_test() tests if starts with "w"
# function should have a parameter for test_string and print the test result

def w_start_test(test_string):
    if test_string.lower().startswith('w'):
        print(test_string + " start with 'w'") 
    else:
        print(test_string + " start with other") 
        
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"


# [ ] Test the 3 string variables provided by calling w_start_test()

w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)


# In[ ]:




