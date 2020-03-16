#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program defines and calls the say_hi & three_three functions
# [ ] review and run the code

def say_hi():
    print("Hello there!")
    print("goodbye")
# end of indentation ends the function

# define three_three 
def three_three():
    print(33) 
    
# calling the functions
say_hi()
print()
three_three()


# In[10]:


# Task2 : Define and call a simple function   yell_it()
# yell_it()   prints the phrase with "!" concatenated to the end
# takes no arguments
# indented function code does the following
# define a variable for called phrase and initialize with a short phrase
# prints phrase as all upper-case letters followed by "!"
# call   yell_it   at the bottom of the cell after the function  def (Tip: no indentation should be used)
# define (def) a simple function called yell_it() and call the function

def yell_it(phrase):
    print(phrase.upper()+"!")
    
yell_it("i love you")


# In[ ]:




